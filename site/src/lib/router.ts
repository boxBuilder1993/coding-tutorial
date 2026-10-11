/**
 * Path-based routing on top of the History API.
 *
 * Every page has a real URL under the site base, e.g.
 *   /coding-tutorial/01-learn-python/02-decisions-and-text/01-true-and-false/
 * The build pre-renders an index.html at each of these paths so the server
 * (GitHub Pages) can serve them and search engines can index them; the app
 * takes over on load. Old hash URLs (#/...) are redirected to the path form.
 */
import { useEffect, useState } from 'react'
import { BASE } from './content'

export type Route =
  | { kind: 'site'; path: string }
  | { kind: 'problem'; id: string }
  | { kind: 'problems' }
  | { kind: 'settings' }

/** Site-relative path with no leading or trailing slash, e.g. "01-learn-python/02-names". */
export function currentPath(pathname: string = window.location.pathname): string {
  let p = pathname
  if (p.startsWith(BASE)) p = p.slice(BASE.length)
  p = p.replace(/^\/+|\/+$/g, '')
  try {
    return decodeURIComponent(p)
  } catch {
    return p
  }
}

export function parseRoute(path: string): Route {
  const p = path.replace(/^\/+|\/+$/g, '')
  if (p === '') return { kind: 'site', path: '' }
  if (p === 'problems') return { kind: 'problems' }
  if (p === 'settings') return { kind: 'settings' }
  if (p.startsWith('problem/')) return { kind: 'problem', id: p.slice('problem/'.length) }
  return { kind: 'site', path: p }
}

export function siteHref(path: string): string {
  return path ? `${BASE}${path}/` : BASE
}

export function problemHref(id: string): string {
  return `${BASE}problem/${id}/`
}

export function problemsHref(): string {
  return `${BASE}problems/`
}

export function settingsHref(): string {
  return `${BASE}settings/`
}

/** Convert a legacy "#/..." route to its path-form href. */
export function hrefFromHash(hash: string): string {
  const p = hash.replace(/^#\/?/, '').replace(/\/+$/, '')
  return p ? `${BASE}${p}/` : BASE
}

const NAVIGATE = 'app:navigate'

/** Push a new in-app URL without reloading. */
export function navigate(href: string) {
  if (href === window.location.pathname) return
  window.history.pushState(null, '', href)
  window.dispatchEvent(new Event(NAVIGATE))
}

/** True when a click on this anchor should be handled in-app. */
function isInternalLink(a: HTMLAnchorElement): boolean {
  if (a.target && a.target !== '_self') return false
  if (a.hasAttribute('download')) return false
  const url = new URL(a.href, window.location.href)
  if (url.origin !== window.location.origin) return false
  if (!url.pathname.startsWith(BASE)) return false
  if (url.hash && url.pathname === window.location.pathname) return false // same-page anchor
  return true
}

/** The current site-relative path, kept in sync with the address bar. */
export function usePath(): string {
  const [path, setPath] = useState(() => {
    // Legacy hash links: rewrite to the path form once, before first render.
    if (window.location.hash.startsWith('#/')) {
      window.history.replaceState(null, '', hrefFromHash(window.location.hash))
    }
    return currentPath()
  })

  useEffect(() => {
    const sync = () => setPath(currentPath())
    // A legacy hash URL applied to an already-open page (e.g. pasted into the
    // address bar) only fires hashchange; rewrite it the same way.
    const onHash = () => {
      if (window.location.hash.startsWith('#/')) {
        window.history.replaceState(null, '', hrefFromHash(window.location.hash))
        sync()
      }
    }
    const onClick = (e: MouseEvent) => {
      if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return
      const a = (e.target as HTMLElement | null)?.closest('a')
      if (!a || !a.getAttribute('href') || !isInternalLink(a)) return
      e.preventDefault()
      navigate(a.pathname)
    }
    window.addEventListener('popstate', sync)
    window.addEventListener('hashchange', onHash)
    window.addEventListener(NAVIGATE, sync)
    document.addEventListener('click', onClick)
    return () => {
      window.removeEventListener('popstate', sync)
      window.removeEventListener('hashchange', onHash)
      window.removeEventListener(NAVIGATE, sync)
      document.removeEventListener('click', onClick)
    }
  }, [])

  return path
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
