/// <reference lib="webworker" />
/* Pyodide lives in this worker so the page stays responsive and can kill a
 * runaway run by terminating the worker. Every job uses fresh globals. */

export const PYODIDE_VERSION = '0.27.7'
const PYODIDE_BASE = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`

export type Chunk = { stream: 'stdout' | 'stderr'; text: string }

export type WorkerIn =
  | { type: 'init'; checkerUrl: string }
  | { type: 'run'; id: number; code: string }
  | { type: 'test'; id: number; code: string; checkSource: string }

export type WorkerOut =
  | { type: 'ready' }
  | { type: 'init-error'; message: string }
  | { type: 'result'; id: number; output: Chunk[]; error: string | null; report: string | null; ms: number }

// eslint-disable-next-line @typescript-eslint/no-explicit-any
let pyodide: any = null
let chunks: Chunk[] = []

function post(msg: WorkerOut) {
  ;(self as unknown as Worker).postMessage(msg)
}

async function init(checkerUrl: string) {
  try {
    const mod = await import(/* @vite-ignore */ PYODIDE_BASE + 'pyodide.mjs')
    pyodide = await mod.loadPyodide({ indexURL: PYODIDE_BASE })
    pyodide.setStdout({ batched: (text: string) => chunks.push({ stream: 'stdout', text: text + '\n' }) })
    pyodide.setStderr({ batched: (text: string) => chunks.push({ stream: 'stderr', text: text + '\n' }) })

    const res = await fetch(checkerUrl)
    if (!res.ok) throw new Error(`could not fetch checker.py (${res.status})`)
    const checker = await res.text()
    pyodide.FS.mkdirTree('/pyl/lib')
    pyodide.FS.mkdirTree('/pyl/work')
    pyodide.FS.writeFile('/pyl/lib/checker.py', checker)
    pyodide.runPython(
      [
        'import sys',
        "sys.path[:0] = ['/pyl/work', '/pyl/lib']",
        'sys.setrecursionlimit(10000)',
        'sys.dont_write_bytecode = True',
      ].join('\n'),
    )
    post({ type: 'ready' })
  } catch (e) {
    post({ type: 'init-error', message: e instanceof Error ? e.message : String(e) })
  }
}

async function run(id: number, code: string) {
  chunks = []
  const t0 = performance.now()
  let error: string | null = null
  const globals = pyodide.globals.get('dict')()
  try {
    await pyodide.runPythonAsync(code, { globals, filename: 'main.py' })
  } catch (e) {
    error = e instanceof Error ? e.message : String(e)
  } finally {
    globals.destroy()
  }
  post({ type: 'result', id, output: chunks, error, report: null, ms: performance.now() - t0 })
}

async function test(id: number, code: string, checkSource: string) {
  chunks = []
  const t0 = performance.now()
  let error: string | null = null
  let report: string | null = null
  try {
    pyodide.FS.writeFile('/pyl/work/solution.py', code)
    const checker = pyodide.pyimport('checker')
    try {
      report = checker._run(checkSource)
    } finally {
      checker.destroy()
    }
  } catch (e) {
    error = e instanceof Error ? e.message : String(e)
  }
  post({ type: 'result', id, output: chunks, error, report, ms: performance.now() - t0 })
}

self.onmessage = (e: MessageEvent<WorkerIn>) => {
  const msg = e.data
  if (msg.type === 'init') void init(msg.checkerUrl)
  else if (msg.type === 'run') void run(msg.id, msg.code)
  else if (msg.type === 'test') void test(msg.id, msg.code, msg.checkSource)
}
