import { useEffect, useState } from 'react'
import { contentUrl } from '../lib/content'
import type { Chunk, WorkerIn, WorkerOut } from './pyodide.worker'

export type { Chunk }
export type RunnerStatus = 'loading' | 'ready' | 'running' | 'error'

export const TIME_BUDGET_MS = 10_000

export interface RunResult {
  output: Chunk[]
  error: string | null
  timedOut: boolean
  ms: number
}

export interface CaseResult {
  name: string
  status: 'pass' | 'fail' | 'error'
  expected?: string
  actual?: string
  message?: string
}

export type TestStatus = 'pass' | 'fail' | 'not-attempted' | 'missing' | 'error' | 'timeout'

export interface TestResult {
  status: TestStatus
  cases: CaseResult[]
  output: Chunk[]
  error: string | null
  missingName: string | null
  ms: number
}

type Pending = { resolve: (r: { output: Chunk[]; error: string | null; report: string | null; ms: number; timedOut: boolean }) => void }

class Runner {
  private worker!: Worker
  private ready!: Promise<void>
  private resolveReady!: () => void
  private pending: Pending | null = null
  private timer: number | null = null
  private nextId = 1
  private chain: Promise<unknown> = Promise.resolve()
  private listeners = new Set<() => void>()
  status: RunnerStatus = 'loading'
  errorMessage: string | null = null

  constructor() {
    this.spawn()
  }

  subscribe(fn: () => void) {
    this.listeners.add(fn)
    return () => {
      this.listeners.delete(fn)
    }
  }

  private setStatus(s: RunnerStatus, message: string | null = null) {
    this.status = s
    this.errorMessage = message
    this.listeners.forEach((fn) => fn())
  }

  private spawn() {
    this.setStatus('loading')
    this.ready = new Promise<void>((res) => (this.resolveReady = res))
    this.worker = new Worker(new URL('./pyodide.worker.ts', import.meta.url), { type: 'module' })
    this.worker.onmessage = (e: MessageEvent<WorkerOut>) => {
      const msg = e.data
      if (msg.type === 'ready') {
        this.setStatus('ready')
        this.resolveReady()
      } else if (msg.type === 'init-error') {
        this.setStatus('error', msg.message)
      } else if (msg.type === 'result') {
        this.finish({ ...msg, timedOut: false })
      }
    }
    this.worker.onerror = (e) => {
      this.setStatus('error', e.message || 'the Python worker crashed')
    }
    this.post({ type: 'init', checkerUrl: contentUrl('checker.py') })
  }

  private post(msg: WorkerIn) {
    this.worker.postMessage(msg)
  }

  private finish(r: { output: Chunk[]; error: string | null; report: string | null; ms: number; timedOut: boolean }) {
    if (this.timer !== null) window.clearTimeout(this.timer)
    this.timer = null
    const p = this.pending
    this.pending = null
    if (this.status !== 'error') this.setStatus('ready')
    p?.resolve(r)
  }

  /** Kill the current run. Pyodide reloads afterwards. */
  stop() {
    if (!this.pending) return
    this.worker.terminate()
    const p = this.pending
    this.pending = null
    if (this.timer !== null) window.clearTimeout(this.timer)
    this.timer = null
    this.spawn()
    p.resolve({ output: [], error: null, report: null, ms: TIME_BUDGET_MS, timedOut: true })
  }

  private exec(make: (id: number) => WorkerIn) {
    const job = this.chain.then(async () => {
      await this.ready
      return new Promise<{ output: Chunk[]; error: string | null; report: string | null; ms: number; timedOut: boolean }>((resolve) => {
        const id = this.nextId++
        this.pending = { resolve }
        this.setStatus('running')
        this.timer = window.setTimeout(() => this.stop(), TIME_BUDGET_MS)
        this.post(make(id))
      })
    })
    this.chain = job.catch(() => undefined)
    return job
  }

  async run(code: string): Promise<RunResult> {
    const r = await this.exec((id) => ({ type: 'run', id, code }))
    return { output: r.output, error: r.error, timedOut: r.timedOut, ms: r.ms }
  }

  async test(code: string, checkSource: string): Promise<TestResult> {
    const r = await this.exec((id) => ({ type: 'test', id, code, checkSource }))
    if (r.timedOut) {
      return { status: 'timeout', cases: [], output: r.output, error: null, missingName: null, ms: r.ms }
    }
    if (!r.report) {
      return { status: 'error', cases: [], output: r.output, error: r.error, missingName: null, ms: r.ms }
    }
    const rep = JSON.parse(r.report) as { status: TestStatus; cases: CaseResult[]; error: string | null; missingName: string | null }
    return { status: rep.status, cases: rep.cases, output: r.output, error: rep.error, missingName: rep.missingName, ms: r.ms }
  }
}

export const runner = new Runner()

export function useRunnerStatus(): { status: RunnerStatus; message: string | null } {
  const [, tick] = useState(0)
  useEffect(() => runner.subscribe(() => tick((n) => n + 1)), [])
  return { status: runner.status, message: runner.errorMessage }
}
