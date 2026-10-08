import type { TestResult } from '../runner/runner'
import { ErrorView, OutputView } from './Output'

export function Results({ result }: { result: TestResult }) {
  const passed = result.cases.filter((c) => c.status === 'pass').length
  let banner: string
  let cls = 'fail'
  switch (result.status) {
    case 'pass':
      banner = `All ${result.cases.length} checks passed.`
      cls = 'pass'
      break
    case 'fail':
      banner = `${passed} of ${result.cases.length} checks passed.`
      break
    case 'not-attempted':
      banner = 'Not attempted yet: your function still raises NotImplementedError.'
      cls = 'neutral'
      break
    case 'missing':
      banner = result.missingName
        ? `Your code must define \`${result.missingName}\`. Check the name and spelling.`
        : 'Your code does not define what the tests import.'
      break
    case 'timeout':
      banner = 'Stopped: the tests ran for more than 10 seconds. Is there an infinite loop?'
      break
    default:
      banner = 'Your code raised an error before the checks could finish.'
  }

  return (
    <div className={`results ${cls}`}>
      <div className="results-banner">{banner}</div>
      {result.cases.length > 0 && (
        <ul className="cases">
          {result.cases.map((c, i) => (
            <li key={i} className={`case ${c.status}`}>
              <span className="case-icon" aria-hidden>
                {c.status === 'pass' ? '✓' : c.status === 'fail' ? '✗' : '!'}
              </span>
              <div className="case-body">
                <div className="case-name">{c.name}</div>
                {c.status === 'fail' && (
                  <div className="case-detail">
                    <div>
                      <span className="label">expected</span> <code>{c.expected}</code>
                    </div>
                    <div>
                      <span className="label">got</span> <code>{c.actual}</code>
                    </div>
                    {c.message && <div className="muted">{c.message}</div>}
                  </div>
                )}
                {c.status === 'error' && c.message && <div className="case-detail muted">{c.message}</div>}
              </div>
            </li>
          ))}
        </ul>
      )}
      <OutputView output={result.output} />
      {result.error && result.status !== 'missing' && <ErrorView traceback={result.error} />}
    </div>
  )
}
