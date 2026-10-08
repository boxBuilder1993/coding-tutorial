import { walkTree, type Content } from '../lib/content'
import { useProgress } from '../lib/progress'
import { problemHref, siteHref } from '../lib/router'

export function ProblemsPage({ content }: { content: Content }) {
  const { progress } = useProgress()
  const usedOn = new Map<string, { path: string; title: string }[]>()
  for (const n of walkTree(content.tree)) {
    for (const id of [...n.problems, ...n.links]) {
      const list = usedOn.get(id) ?? []
      if (!list.some((x) => x.path === n.path)) list.push({ path: n.path, title: n.title })
      usedOn.set(id, list)
    }
  }
  const problems = Object.values(content.problems).sort((a, b) => a.title.localeCompare(b.title))
  const solved = problems.filter((p) => progress.problems[p.id]?.status === 'solved').length

  return (
    <article className="page">
      <h1>All problems</h1>
      <p className="muted">
        {solved} of {problems.length} solved.
      </p>
      <table className="problems-table">
        <thead>
          <tr>
            <th>Problem</th>
            <th>Status</th>
            <th>Appears in</th>
          </tr>
        </thead>
        <tbody>
          {problems.map((p) => {
            const pr = progress.problems[p.id]
            const st = pr?.status ?? 'not-started'
            const label = st === 'solved' ? (pr.hintsUsed > 0 || pr.revealed ? 'Solved with help' : 'Solved') : st === 'in-progress' ? 'In progress' : 'Not started'
            return (
              <tr key={p.id}>
                <td>
                  <a href={problemHref(p.id)}>{p.title}</a>
                </td>
                <td>
                  <span className={`status-pill ${st}`}>{label}</span>
                </td>
                <td>
                  {(usedOn.get(p.id) ?? []).map((u, i) => (
                    <span key={u.path}>
                      {i > 0 && ', '}
                      <a href={siteHref(u.path)}>{u.title}</a>
                    </span>
                  ))}
                </td>
              </tr>
            )
          })}
        </tbody>
      </table>
    </article>
  )
}
