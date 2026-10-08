import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState, type ReactNode } from 'react'

export type ProblemStatus = 'not-started' | 'in-progress' | 'solved'

export interface ProblemProgress {
  status: ProblemStatus
  code: string | null
  hintsUsed: number
  revealed: boolean
  firstSolved: string | null
  attempts: number
}

export interface Progress {
  version: 1
  lastRoute: string
  problems: Record<string, ProblemProgress>
}

const KEY = 'pyl.progress.v1'

export const emptyProblem: ProblemProgress = {
  status: 'not-started',
  code: null,
  hintsUsed: 0,
  revealed: false,
  firstSolved: null,
  attempts: 0,
}

function emptyProgress(): Progress {
  return { version: 1, lastRoute: '', problems: {} }
}

function load(): Progress {
  try {
    const raw = localStorage.getItem(KEY)
    if (!raw) return emptyProgress()
    const parsed = JSON.parse(raw)
    if (parsed && parsed.version === 1 && typeof parsed.problems === 'object') {
      return { version: 1, lastRoute: parsed.lastRoute ?? '', problems: parsed.problems }
    }
  } catch {
    /* corrupt or unavailable storage: start fresh */
  }
  return emptyProgress()
}

function save(p: Progress) {
  try {
    localStorage.setItem(KEY, JSON.stringify(p))
  } catch {
    /* storage full or blocked; keep going in memory */
  }
}

interface ProgressApi {
  progress: Progress
  problem: (id: string) => ProblemProgress
  update: (id: string, patch: Partial<ProblemProgress> | ((p: ProblemProgress) => Partial<ProblemProgress>)) => void
  setLastRoute: (route: string) => void
  exportJson: () => string
  importJson: (json: string) => string | null
  reset: () => void
}

const Ctx = createContext<ProgressApi | null>(null)

export function ProgressProvider({ children }: { children: ReactNode }) {
  const [progress, setProgress] = useState<Progress>(load)
  const first = useRef(true)

  useEffect(() => {
    if (first.current) {
      first.current = false
      return
    }
    save(progress)
  }, [progress])

  const problem = useCallback((id: string) => progress.problems[id] ?? emptyProblem, [progress])

  const update = useCallback<ProgressApi['update']>((id, patch) => {
    setProgress((prev) => {
      const cur = prev.problems[id] ?? emptyProblem
      const next = typeof patch === 'function' ? patch(cur) : patch
      return { ...prev, problems: { ...prev.problems, [id]: { ...cur, ...next } } }
    })
  }, [])

  const setLastRoute = useCallback((route: string) => {
    setProgress((prev) => (prev.lastRoute === route ? prev : { ...prev, lastRoute: route }))
  }, [])

  const exportJson = useCallback(() => JSON.stringify(progress, null, 2), [progress])

  const importJson = useCallback((json: string): string | null => {
    try {
      const parsed = JSON.parse(json)
      if (!parsed || parsed.version !== 1 || typeof parsed.problems !== 'object') {
        return 'That file is not a progress export from this site.'
      }
      setProgress({ version: 1, lastRoute: parsed.lastRoute ?? '', problems: parsed.problems })
      return null
    } catch {
      return 'That file is not valid JSON.'
    }
  }, [])

  const reset = useCallback(() => setProgress(emptyProgress()), [])

  const api = useMemo<ProgressApi>(
    () => ({ progress, problem, update, setLastRoute, exportJson, importJson, reset }),
    [progress, problem, update, setLastRoute, exportJson, importJson, reset],
  )
  return <Ctx.Provider value={api}>{children}</Ctx.Provider>
}

export function useProgress(): ProgressApi {
  const api = useContext(Ctx)
  if (!api) throw new Error('useProgress outside ProgressProvider')
  return api
}
