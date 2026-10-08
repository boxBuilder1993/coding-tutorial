import { useState } from 'react'
import { runner, useRunnerStatus, type RunResult } from '../runner/runner'
import { CodeEditor } from './CodeEditor'
import { ErrorView, OutputView } from './Output'

export function PlayBlock({ code: initial }: { code: string }) {
  const [code, setCode] = useState(initial)
  const [result, setResult] = useState<RunResult | null>(null)
  const [running, setRunning] = useState(false)
  const { status } = useRunnerStatus()

  const run = async () => {
    if (running) return
    setRunning(true)
    setResult(null)
    try {
      setResult(await runner.run(code))
    } finally {
      setRunning(false)
    }
  }

  const ready = status === 'ready' || status === 'running'
  const lines = Math.max(2, initial.split('\n').length)

  return (
    <div className="play">
      <CodeEditor value={code} onChange={setCode} onRun={run} minLines={lines} ariaLabel="Example code" />
      <div className="toolbar">
        {running ? (
          <button type="button" className="danger" onClick={() => runner.stop()}>
            Stop
          </button>
        ) : (
          <button type="button" className="primary" onClick={run} disabled={!ready} title="Ctrl/Cmd + Enter">
            {status === 'loading' ? 'Loading Python…' : status === 'error' ? 'Python unavailable' : 'Run'}
          </button>
        )}
        {code !== initial && (
          <button type="button" className="linkish" onClick={() => setCode(initial)}>
            Reset
          </button>
        )}
        <span className="hint-key">Ctrl/⌘ + Enter</span>
      </div>
      {result && (
        <div className="play-result">
          {result.timedOut && <div className="error-summary">Stopped: your code ran for more than 10 seconds. Is there an infinite loop?</div>}
          <OutputView output={result.output} />
          {result.error && <ErrorView traceback={result.error} />}
          {!result.timedOut && !result.error && result.output.length === 0 && (
            <div className="muted">Finished with no output. Use print() to show something.</div>
          )}
        </div>
      )}
    </div>
  )
}
