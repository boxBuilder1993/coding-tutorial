import { useRef, useState } from 'react'
import { useProgress } from '../lib/progress'
import { PYODIDE_VERSION } from '../runner/pyodide.worker'
import { useRunnerStatus } from '../runner/runner'

export function SettingsPage() {
  const { exportJson, importJson, reset, progress } = useProgress()
  const [message, setMessage] = useState<string | null>(null)
  const file = useRef<HTMLInputElement>(null)
  const { status, message: runnerMessage } = useRunnerStatus()

  const doExport = () => {
    const blob = new Blob([exportJson()], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `learn-python-progress-${new Date().toISOString().slice(0, 10)}.json`
    a.click()
    URL.revokeObjectURL(url)
  }

  const doImport = async (f: File | undefined) => {
    if (!f) return
    const err = importJson(await f.text())
    setMessage(err ?? 'Progress imported.')
    if (file.current) file.current.value = ''
  }

  const doReset = () => {
    if (window.confirm('Delete all progress and saved code in this browser? This cannot be undone.')) {
      reset()
      setMessage('Progress cleared.')
    }
  }

  const count = Object.keys(progress.problems).length

  return (
    <article className="page">
      <h1>Settings</h1>

      <h2>Progress</h2>
      <p className="muted">
        Progress is stored only in this browser. {count} problem{count === 1 ? '' : 's'} have saved state.
      </p>
      <div className="toolbar">
        <button type="button" className="primary" onClick={doExport}>
          Export progress
        </button>
        <button type="button" onClick={() => file.current?.click()}>
          Import progress…
        </button>
        <input ref={file} type="file" accept="application/json,.json" hidden onChange={(e) => doImport(e.target.files?.[0])} />
        <button type="button" className="danger" onClick={doReset}>
          Reset everything
        </button>
      </div>
      {message && <p className="muted">{message}</p>}

      <h2>Python runtime</h2>
      <p className="muted">
        Pyodide {PYODIDE_VERSION}, status: {status}
        {runnerMessage ? ` (${runnerMessage})` : ''}. Python runs entirely in your browser; nothing you type is sent anywhere.
      </p>
    </article>
  )
}
