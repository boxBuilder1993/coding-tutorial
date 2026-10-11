import { useEffect, useState } from 'react'
import { fetchPage, findNode, walkTree, type Content } from '../lib/content'
import { useProgress } from '../lib/progress'
import { hrefFromHash, siteHref } from '../lib/router'
import { Markdown } from '../components/Markdown'

/**
 * A site page. `url` is the clean route path ("learn-python/names"); the
 * node found for it carries the folder path ("01-learn-python/02-names")
 * that the markdown is fetched from and that relative links resolve against.
 */
export function SitePage({ content, url }: { content: Content; url: string }) {
  // Keep the markdown and the page it belongs to together, so a page is
  // never rendered with another page's text during navigation.
  const [loaded, setLoaded] = useState<{ url: string; text: string } | null>(null)
  const [error, setError] = useState<string | null>(null)
  const { progress } = useProgress()
  const node = findNode(content.tree, url)
  const md = loaded?.url === url ? loaded.text : null

  useEffect(() => {
    if (!node) return
    let alive = true
    setError(null)
    fetchPage(node.path).then(
      (t) => alive && setLoaded({ url, text: t }),
      (e) => alive && setError(e instanceof Error ? e.message : String(e)),
    )
    return () => {
      alive = false
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [url])

  if (!node) {
    return (
      <article className="page">
        <h1>Page not found</h1>
        <p>
          There is no page at <code>{url}</code>. <a href={siteHref('')}>Go home</a>.
        </p>
      </article>
    )
  }

  const flat = [...walkTree(content.tree)]
  const idx = flat.findIndex((n) => n.url === url)
  const prev = idx > 0 ? flat[idx - 1] : null
  const next = idx >= 0 && idx < flat.length - 1 ? flat[idx + 1] : null
  const crumbs = url ? url.split('/').map((_, i, parts) => parts.slice(0, i + 1).join('/')) : []
  // lastRoute may be a legacy "#/..." value from before path routing.
  const last = progress.lastRoute.startsWith('#') ? hrefFromHash(progress.lastRoute) : progress.lastRoute
  const resume = url === '' && last && last !== siteHref('') ? last : null

  return (
    <article className="page" data-path={url}>
      {crumbs.length > 1 && (
        <nav className="crumbs" aria-label="Breadcrumb">
          <a href={siteHref('')}>Home</a>
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
      {md !== null && <Markdown source={md} pagePath={node.path} problems={content.problems} />}
      <nav className="pager">
        {prev ? <a href={siteHref(prev.url)}>← {prev.title}</a> : <span />}
        {next ? <a href={siteHref(next.url)}>{next.title} →</a> : <span />}
      </nav>
    </article>
  )
}
