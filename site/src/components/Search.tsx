import { useEffect, useRef, useState } from 'react'
import { loadIndex, search, type SearchEntry, type SearchHit } from '../lib/search'
import { problemHref, siteHref } from '../lib/router'

export function Search({ onNavigate }: { onNavigate?: () => void }) {
  const [query, setQuery] = useState('')
  const [index, setIndex] = useState<SearchEntry[] | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [hits, setHits] = useState<SearchHit[]>([])
  const [active, setActive] = useState(0)
  const input = useRef<HTMLInputElement>(null)

  const ensureIndex = () => {
    if (index || error) return
    loadIndex().then(setIndex, (e) => setError(e instanceof Error ? e.message : String(e)))
  }

  useEffect(() => {
    if (!index) {
      if (query) ensureIndex()
      return
    }
    setHits(search(index, query))
    setActive(0)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [query, index])

  // "/" focuses the search box from anywhere except an editor or input.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key !== '/' || e.ctrlKey || e.metaKey || e.altKey) return
      const t = e.target as HTMLElement | null
      if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return
      e.preventDefault()
      input.current?.focus()
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])

  const hrefFor = (h: SearchHit) => (h.entry.kind === 'page' ? siteHref(h.entry.id) : problemHref(h.entry.id))

  const go = (h: SearchHit) => {
    window.location.hash = hrefFor(h)
    setQuery('')
    onNavigate?.()
  }

  const onKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault()
      setActive((a) => Math.min(hits.length - 1, a + 1))
    } else if (e.key === 'ArrowUp') {
      e.preventDefault()
      setActive((a) => Math.max(0, a - 1))
    } else if (e.key === 'Enter' && hits[active]) {
      e.preventDefault()
      go(hits[active])
    } else if (e.key === 'Escape') {
      setQuery('')
      input.current?.blur()
    }
  }

  const open = query.trim().length > 0

  return (
    <div className="search">
      <input
        ref={input}
        type="search"
        className="search-input"
        placeholder="Search lessons  ( / )"
        aria-label="Search lessons and problems"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onFocus={ensureIndex}
        onKeyDown={onKeyDown}
        autoComplete="off"
      />
      {open && (
        <div className="search-results" role="listbox" aria-label="Search results">
          {error && <div className="search-empty">Search is unavailable: {error}</div>}
          {!error && !index && <div className="search-empty muted">Loading…</div>}
          {index && hits.length === 0 && <div className="search-empty muted">Nothing matches “{query}”.</div>}
          {hits.map((h, i) => (
            <a
              key={h.entry.kind + h.entry.id}
              href={hrefFor(h)}
              className={`search-hit ${i === active ? 'active' : ''}`}
              role="option"
              aria-selected={i === active}
              onMouseEnter={() => setActive(i)}
              onClick={(e) => {
                e.preventDefault()
                go(h)
              }}
            >
              <div className="search-hit-title">
                {h.entry.title}
                <span className="search-kind">{h.entry.kind === 'page' ? 'lesson' : 'problem'}</span>
              </div>
              <div className="search-snippet">{h.snippet}</div>
            </a>
          ))}
        </div>
      )}
    </div>
  )
}
