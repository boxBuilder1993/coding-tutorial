import { useEffect, useRef, useState } from 'react'
import { fetchCheck, stripTitle, type Problem } from '../lib/content'
import { useProgress } from '../lib/progress'
import { problemHref } from '../lib/router'
import { runner, useRunnerStatus, type TestResult } from '../runner/runner'
import { CodeEditor } from './CodeEditor'
import { Markdown } from './Markdown'
import { Results } from './Results'

interface Props {
  problem: Problem
  layout: 'stacked' | 'split'
}

export function ExerciseCard({ problem, layout }: Props) {
  const { problem: getProgress, update } = useProgress()
  const prog = getProgress(problem.id)
  const [code, setCode] = useState(prog.code ?? problem.starter)
  const [result, setResult] = useState<TestResult | null>(null)
  const [running, setRunning] = useState(false)
  const [showApproach, setShowApproach] = useState(false)
  const { status } = useRunnerStatus()
  const saveTimer = useRef<number | null>(null)

  // Debounced autosave of the editor contents.
  useEffect(() => {
    if (code === (prog.code ?? problem.starter)) return
    if (saveTimer.current) window.clearTimeout(saveTimer.current)
    saveTimer.current = window.setTimeout(() => {
      update(problem.id, (p) => ({ code, status: p.status === 'not-started' ? 'in-progress' : p.status }))
    }, 400)
    return () => {
      if (saveTimer.current) window.clearTimeout(saveTimer.current)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [code])

  const run = async () => {
    if (running) return
    setRunning(true)
    setResult(null)
    try {
      const check = await fetchCheck(problem.id)
      const r = await runner.test(code, check)
      setResult(r)
      update(problem.id, (p) => ({
        code,
        attempts: p.attempts + 1,
        status: r.status === 'pass' ? 'solved' : p.status === 'solved' ? 'solved' : 'in-progress',
        firstSolved: r.status === 'pass' && !p.firstSolved ? new Date().toISOString() : p.firstSolved,
      }))
    } catch (e) {
      setResult({
        status: 'error',
        cases: [],
        output: [],
        error: e instanceof Error ? e.message : String(e),
        missingName: null,
        ms: 0,
      })
    } finally {
      setRunning(false)
    }
  }

  const reset = () => {
    if (code !== problem.starter && !window.confirm('Replace your code with the starter code?')) return
    setCode(problem.starter)
    setResult(null)
    update(problem.id, { code: null })
  }

  const revealHint = () => update(problem.id, (p) => ({ hintsUsed: Math.min(problem.hints.length, p.hintsUsed + 1) }))
  const allHintsUsed = prog.hintsUsed >= problem.hints.length
  const unlocked = prog.status === 'solved' || prog.revealed
  const canReveal = allHintsUsed && !unlocked
  const reveal = () => {
    update(problem.id, { revealed: true })
    setShowApproach(true)
  }

  const ready = status === 'ready' || status === 'running'
  const statusLabel = prog.status === 'solved' ? (prog.hintsUsed > 0 || prog.revealed ? 'Solved with help' : 'Solved') : prog.status === 'in-progress' ? 'In progress' : 'Not started'

  return (
    <section className={`exercise ${layout}`} aria-label={problem.title}>
      <div className="exercise-statement">
        <header className="exercise-header">
          <h3>
            {layout === 'stacked' ? <a href={problemHref(problem.id)}>{problem.title}</a> : problem.title}
          </h3>
          <span className={`status-pill ${prog.status}`}>{statusLabel}</span>
        </header>
        <Markdown source={stripTitle(problem.statement)} pagePath="" runnable={false} />

        {problem.hints.length > 0 && (
          <div className="hints">
            <h4>Hints</h4>
            <ol>
              {problem.hints.slice(0, prog.hintsUsed).map((h, i) => (
                <li key={i}>
                  <Markdown source={h} pagePath="" runnable={false} />
                </li>
              ))}
            </ol>
            {!allHintsUsed && (
              <button type="button" className="linkish" onClick={revealHint}>
                Show hint {prog.hintsUsed + 1} of {problem.hints.length}
              </button>
            )}
          </div>
        )}

        {(unlocked || canReveal) && (
          <div className="approach">
            {unlocked ? (
              <>
                <button type="button" className="linkish" onClick={() => setShowApproach((s) => !s)}>
                  {showApproach ? 'Hide approach and reference' : 'Show approach and reference'}
                </button>
                {showApproach && (
                  <div className="approach-body">
                    {problem.approach && (
                      <>
                        <h4>Approach</h4>
                        <Markdown source={problem.approach} pagePath="" runnable={false} />
                      </>
                    )}
                    <h4>Reference solution</h4>
                    <pre className="static lang-python">
                      <code>{problem.reference}</code>
                    </pre>
                  </div>
                )}
              </>
            ) : (
              <button type="button" className="linkish" onClick={reveal}>
                Still stuck? Show the approach
              </button>
            )}
          </div>
        )}
      </div>

      <div className="exercise-editor">
        <CodeEditor value={code} onChange={setCode} onRun={run} minLines={8} ariaLabel={`Solution for ${problem.title}`} />
        <div className="toolbar">
          {running ? (
            <button type="button" className="danger" onClick={() => runner.stop()}>
              Stop
            </button>
          ) : (
            <button type="button" className="primary" onClick={run} disabled={!ready} title="Ctrl/Cmd + Enter">
              {status === 'loading' ? 'Loading Python…' : status === 'error' ? 'Python unavailable' : 'Run tests'}
            </button>
          )}
          <button type="button" className="linkish" onClick={reset}>
            Reset to starter
          </button>
          <span className="hint-key">Ctrl/⌘ + Enter</span>
        </div>
        {result && <Results result={result} />}
      </div>
    </section>
  )
}
