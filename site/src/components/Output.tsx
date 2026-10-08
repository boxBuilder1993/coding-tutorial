import { useState } from 'react'
import type { Chunk } from '../runner/runner'
import { cleanTraceback, summarize } from '../lib/errors'

export function OutputView({ output }: { output: Chunk[] }) {
  if (output.length === 0) return null
  return (
    <pre className="output">
      {output.map((c, i) => (
        <span key={i} className={c.stream === 'stderr' ? 'stderr' : undefined}>
          {c.text}
        </span>
      ))}
    </pre>
  )
}

export function ErrorView({ traceback, lead }: { traceback: string; lead?: string }) {
  const [open, setOpen] = useState(false)
  const clean = cleanTraceback(traceback)
  return (
    <div className="error">
      <div className="error-summary">{lead ?? summarize(clean)}</div>
      <button type="button" className="linkish" onClick={() => setOpen((o) => !o)}>
        {open ? 'Hide details' : 'Show details'}
      </button>
      {open && <pre className="traceback">{clean}</pre>}
    </div>
  )
}
