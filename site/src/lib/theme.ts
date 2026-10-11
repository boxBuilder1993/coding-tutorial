import { useEffect, useState } from 'react'

export type ThemeChoice = 'system' | 'light' | 'dark'

const KEY = 'pyl.theme'
const listeners = new Set<() => void>()
const media = window.matchMedia('(prefers-color-scheme: dark)')

function read(): ThemeChoice {
  try {
    const v = localStorage.getItem(KEY)
    if (v === 'light' || v === 'dark' || v === 'system') return v
  } catch {
    /* storage unavailable */
  }
  return 'system'
}

let choice: ThemeChoice = read()

function apply() {
  const root = document.documentElement
  if (choice === 'system') root.removeAttribute('data-theme')
  else root.setAttribute('data-theme', choice)
  listeners.forEach((fn) => fn())
}

export function getTheme(): ThemeChoice {
  return choice
}

export function setTheme(next: ThemeChoice) {
  choice = next
  try {
    localStorage.setItem(KEY, next)
  } catch {
    /* ignore */
  }
  apply()
}

/** Whether the page is currently rendered dark, after resolving "system". */
export function isDark(): boolean {
  return choice === 'dark' || (choice === 'system' && media.matches)
}

export function subscribeTheme(fn: () => void) {
  listeners.add(fn)
  return () => {
    listeners.delete(fn)
  }
}

media.addEventListener('change', () => listeners.forEach((fn) => fn()))
apply()

export function useTheme(): { choice: ThemeChoice; dark: boolean; set: (t: ThemeChoice) => void } {
  const [, tick] = useState(0)
  useEffect(() => subscribeTheme(() => tick((n) => n + 1)), [])
  return { choice, dark: isDark(), set: setTheme }
}
