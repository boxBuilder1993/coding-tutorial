import { useEffect, useState } from 'react'

export function TutorPrompt({ prompt }: { prompt: string }) {
  const [open, setOpen] = useState(false)
  const [copied, setCopied] = useState<'idle' | 'done' | 'failed'>('idle')

  useEffect(() => {
    if (copied === 'idle') return
    const t = window.setTimeout(() => setCopied('idle'), 2000)
    return () => window.clearTimeout(t)
  }, [copied])

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(prompt)
      setCopied('done')
    } catch {
      setCopied('failed')
      setOpen(true)
    }
  }

  return (
    <div className="tutor">
      <div className="toolbar tutor-bar">
        <button type="button" onClick={copy} title="Copy a prompt that turns an AI assistant into a tutor for this exercise">
          {copied === 'done' ? 'Copied' : copied === 'failed' ? 'Select and copy below' : 'Copy tutor prompt'}
        </button>
        <button type="button" className="linkish" onClick={() => setOpen((o) => !o)}>
          {open ? 'Hide prompt' : 'What is this?'}
        </button>
      </div>
      {open && (
        <div className="tutor-panel">
          <p className="muted">
            Stuck and have an AI assistant? Paste this prompt into it. It contains your code, your last results, and
            instructions that make the assistant ask questions instead of giving you the answer. It is copied to your
            clipboard only; this site sends nothing anywhere. If the assistant gives you code anyway, close it and come back.
          </p>
          <textarea className="tutor-text" readOnly value={prompt} rows={14} onFocus={(e) => e.currentTarget.select()} />
        </div>
      )}
    </div>
  )
}
