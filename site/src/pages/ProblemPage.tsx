import { walkTree, type Content } from '../lib/content'
import { problemsHref, siteHref } from '../lib/router'
import { ExerciseCard } from '../components/ExerciseCard'

export function ProblemPage({ content, id }: { content: Content; id: string }) {
  const problem = content.problems[id]
  if (!problem) {
    return (
      <article className="page">
        <h1>Problem not found</h1>
        <p>
          There is no problem called <code>{id}</code>. <a href={problemsHref()}>See all problems</a>.
        </p>
      </article>
    )
  }
  const pages = [...walkTree(content.tree)].filter((n) => n.problems.includes(id) || n.links.includes(id))
  return (
    <article className="page page-wide">
      <nav className="crumbs" aria-label="Breadcrumb">
        <a href={problemsHref()}>All problems</a>
        {pages.length > 0 && (
          <>
            {' · appears in '}
            {pages.map((n, i) => (
              <span key={n.url}>
                {i > 0 && ', '}
                <a href={siteHref(n.url)}>{n.title}</a>
              </span>
            ))}
          </>
        )}
      </nav>
      <ExerciseCard key={id} problem={problem} layout="split" />
    </article>
  )
}
