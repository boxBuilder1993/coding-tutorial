import { useEffect, useState } from 'react'
import { fetchPage, findNode, walkTree, type Content } from '../lib/content'
import { useProgress } from '../lib/progress'
import { siteHref } from '../lib/router'
import { Markdown } from '../components/Markdown'

export function SitePage({ content, path }: { content: Content; path: string }) {
  const [md, setMd] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)
  const { progress } = useProgress()

  useEffect(() => {
    let alive = true
    setMd(null)
    setError(null)
    fetchPage(path).then(
      (t) => alive && setMd(t),
      (e) => alive && setError(e instanceof Error ? e.message : String(e)),
    )
    return () => {
      alive = false
    }
  }, [path])

  const node = findNode(content.tree, path)
  if (!node) {
    return (
      <article className="page">
        <h1>Page not found</h1>
        <p>
          There is no page at <code>{path}</code>. <a href="#/">Go home</a>.
        </p>
      </article>
    )
  }

  const flat = [...walkTree(content.tree)]
  const idx = flat.findIndex((n) => n.path === path)
  const prev = idx > 0 ? flat[idx - 1] : null
  const next = idx >= 0 && idx < flat.length - 1 ? flat[idx + 1] : null
  const crumbs = path ? path.split('/').map((_, i, parts) => parts.slice(0, i + 1).join('/')) : []
  const resume = path === '' && progress.lastRoute && progress.lastRoute !== '#/' ? progress.lastRoute : null

  return (
    <article className="page">
      {crumbs.length > 1 && (
        <nav className="crumbs" aria-label="Breadcrumb">
          <a href="#/">Home</a>
          {crumbs.slice(0, -1).map((p) => (
            <span key={p}>
              {' / '}
              <a href={siteHref(p)}>{findNode(content.tree, p)?.title ?? p}</a>
            </span>
          ))}
        </nav>
      )}
      {resume && (
        <div className="resume">
          <a href={resume}>Continue where you left off →</a>
        </div>
      )}
      {error && <div className="error-summary">Could not load this page: {error}</div>}
      {md === null && !error && <div className="muted">Loading…</div>}
      {md !== null && <Markdown source={md} pagePath={path} problems={content.problems} />}
      <nav className="pager">
        {prev ? <a href={siteHref(prev.path)}>← {prev.title}</a> : <span />}
        {next ? <a href={siteHref(next.path)}>{next.title} →</a> : <span />}
      </nav>
    </article>
  )
}
