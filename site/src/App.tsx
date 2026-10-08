import { useEffect, useState } from 'react'
import { loadContent, type Content } from './lib/content'
import { ProgressProvider, useProgress } from './lib/progress'
import { parseRoute, useHash } from './lib/router'
import { useRunnerStatus } from './runner/runner'
import { Sidebar } from './components/Sidebar'
import { SitePage } from './pages/SitePage'
import { ProblemPage } from './pages/ProblemPage'
import { ProblemsPage } from './pages/ProblemsPage'
import { SettingsPage } from './pages/SettingsPage'

function RunnerPill() {
  const { status, message } = useRunnerStatus()
  const label = status === 'loading' ? 'Loading Python…' : status === 'ready' ? 'Python ready' : status === 'running' ? 'Running…' : 'Python unavailable'
  return (
    <span className={`runner-pill ${status}`} title={message ?? undefined}>
      {label}
    </span>
  )
}

function Shell({ content }: { content: Content }) {
  const hash = useHash()
  const route = parseRoute(hash)
  const { setLastRoute } = useProgress()
  const [drawer, setDrawer] = useState(false)

  useEffect(() => {
    setLastRoute(hash)
    window.scrollTo(0, 0)
    document.title = route.kind === 'site' && route.path === '' ? content.tree.title : `${titleFor()} · ${content.tree.title}`
    function titleFor() {
      if (route.kind === 'problem') return content.problems[route.id]?.title ?? 'Problem'
      if (route.kind === 'problems') return 'All problems'
      if (route.kind === 'settings') return 'Settings'
      let t = 'Page'
      const stack = [content.tree]
      while (stack.length) {
        const n = stack.pop()!
        if (n.path === route.path) {
          t = n.title
          break
        }
        stack.push(...n.children)
      }
      return t
    }
  }, [hash, route, content, setLastRoute])

  let page
  switch (route.kind) {
    case 'problem':
      page = <ProblemPage content={content} id={route.id} />
      break
    case 'problems':
      page = <ProblemsPage content={content} />
      break
    case 'settings':
      page = <SettingsPage />
      break
    default:
      page = <SitePage content={content} path={route.path} />
  }

  return (
    <div className={`app ${drawer ? 'drawer-open' : ''}`}>
      <header className="topbar">
        <button type="button" className="menu" aria-label="Toggle contents" onClick={() => setDrawer((d) => !d)}>
          ☰
        </button>
        <a className="brand" href="#/">
          {content.tree.title}
        </a>
        <RunnerPill />
      </header>
      <Sidebar tree={content.tree} route={route} onNavigate={() => setDrawer(false)} />
      {drawer && <div className="scrim" onClick={() => setDrawer(false)} />}
      <main className="main">{page}</main>
    </div>
  )
}

export default function App() {
  const [content, setContent] = useState<Content | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    loadContent().then(setContent, (e) => setError(e instanceof Error ? e.message : String(e)))
  }, [])

  if (error) {
    return (
      <div className="boot">
        <h1>Could not load content</h1>
        <p>{error}</p>
        <p className="muted">
          If you are developing locally, run <code>python3 scripts/build_content.py</code> from the repository root first.
        </p>
      </div>
    )
  }
  if (!content) return <div className="boot muted">Loading…</div>
  return (
    <ProgressProvider>
      <Shell content={content} />
    </ProgressProvider>
  )
}
