import { useEffect, useState } from 'react'

export type Route =
  | { kind: 'site'; path: string }
  | { kind: 'problem'; id: string }
  | { kind: 'problems' }
  | { kind: 'settings' }

export function parseRoute(hash: string): Route {
  const raw = hash.replace(/^#\/?/, '').replace(/\/+$/, '')
  const p = decodeURIComponent(raw)
  if (p === '') return { kind: 'site', path: '' }
  if (p === 'problems') return { kind: 'problems' }
  if (p === 'settings') return { kind: 'settings' }
  if (p.startsWith('problem/')) return { kind: 'problem', id: p.slice('problem/'.length) }
  return { kind: 'site', path: p }
}

export function useHash(): string {
  const [hash, setHash] = useState(window.location.hash || '#/')
  useEffect(() => {
    const onChange = () => setHash(window.location.hash || '#/')
    window.addEventListener('hashchange', onChange)
    return () => window.removeEventListener('hashchange', onChange)
  }, [])
  return hash
}

export function siteHref(path: string): string {
  return path ? `#/${path}` : '#/'
}

export function problemHref(id: string): string {
  return `#/problem/${id}`
}

/** Resolve a relative markdown link against the current site page path. */
export function resolveSiteLink(href: string, pagePath: string): string | null {
  if (/^[a-z][a-z0-9+.-]*:/i.test(href) || href.startsWith('#') || href.startsWith('/')) return null
  const base = 'http://x/' + (pagePath ? pagePath + '/' : '')
  let path: string
  try {
    path = new URL(href, base).pathname
  } catch {
    return null
  }
  path = path.replace(/\/README\.md$/i, '').replace(/^\/+|\/+$/g, '')
  return siteHref(path)
}
