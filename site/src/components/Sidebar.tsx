import { useEffect, useState } from 'react'
import type { TreeNode } from '../lib/content'
import { useProgress } from '../lib/progress'
import { siteHref, type Route } from '../lib/router'

interface Props {
  tree: TreeNode
  route: Route
  onNavigate?: () => void
}

type PageStatus = 'none' | 'todo' | 'partial' | 'done'

export function Sidebar({ tree, route, onNavigate }: Props) {
  const { progress } = useProgress()
  const current = route.kind === 'site' ? route.path : null
  const [expanded, setExpanded] = useState<Set<string>>(() => new Set())

  // Expand ancestors of the current page.
  useEffect(() => {
    if (current === null) return
    const parts = current.split('/')
    setExpanded((prev) => {
      const next = new Set(prev)
      for (let i = 1; i <= parts.length; i++) next.add(parts.slice(0, i).join('/'))
      return next
    })
  }, [current])

  const pageStatus = (n: TreeNode): PageStatus => {
    if (n.problems.length === 0) return 'none'
    const solved = n.problems.filter((id) => progress.problems[id]?.status === 'solved').length
    if (solved === 0) return 'todo'
    return solved === n.problems.length ? 'done' : 'partial'
  }

  const toggle = (path: string) =>
    setExpanded((prev) => {
      const next = new Set(prev)
      if (next.has(path)) next.delete(path)
      else next.add(path)
      return next
    })

  const renderNode = (n: TreeNode, depth: number) => {
    const isCurrent = current === n.path
    const hasChildren = n.children.length > 0
    const open = expanded.has(n.path)
    const st = pageStatus(n)
    return (
      <li key={n.path} className={`nav-item depth-${depth}`}>
        <div className={`nav-row ${isCurrent ? 'current' : ''}`}>
          {hasChildren ? (
            <button type="button" className="disclosure" aria-label={open ? 'Collapse' : 'Expand'} aria-expanded={open} onClick={() => toggle(n.path)}>
              {open ? '▾' : '▸'}
            </button>
          ) : (
            <span className="disclosure-spacer" />
          )}
          <a href={siteHref(n.path)} onClick={onNavigate} aria-current={isCurrent ? 'page' : undefined}>
            {n.title}
          </a>
          {st !== 'none' && (
            <span className={`page-status ${st}`} title={st === 'done' ? 'All exercises solved' : st === 'partial' ? 'Some exercises solved' : 'Exercises not started'} aria-hidden>
              {st === 'done' ? '●' : st === 'partial' ? '◐' : '○'}
            </span>
          )}
        </div>
        {hasChildren && open && <ul>{n.children.map((c) => renderNode(c, depth + 1))}</ul>}
      </li>
    )
  }

  return (
    <nav className="sidebar" aria-label="Contents">
      <ul className="nav-root">
        <li className="nav-item depth-0">
          <div className={`nav-row ${current === '' ? 'current' : ''}`}>
            <span className="disclosure-spacer" />
            <a href="#/" onClick={onNavigate} aria-current={current === '' ? 'page' : undefined}>
              {tree.title}
            </a>
          </div>
        </li>
        {tree.children.map((c) => renderNode(c, 0))}
      </ul>
      <ul className="nav-root nav-extra">
        <li className="nav-item depth-0">
          <div className={`nav-row ${route.kind === 'problems' ? 'current' : ''}`}>
            <span className="disclosure-spacer" />
            <a href="#/problems" onClick={onNavigate}>All problems</a>
          </div>
        </li>
        <li className="nav-item depth-0">
          <div className={`nav-row ${route.kind === 'settings' ? 'current' : ''}`}>
            <span className="disclosure-spacer" />
            <a href="#/settings" onClick={onNavigate}>Settings</a>
          </div>
        </li>
      </ul>
    </nav>
  )
}
