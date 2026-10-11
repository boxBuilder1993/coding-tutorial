import { contentUrl } from './content'

export interface SearchEntry {
  kind: 'page' | 'problem'
  id: string
  title: string
  headings: string[]
  text: string
}

export interface SearchHit {
  entry: SearchEntry
  score: number
  snippet: string
}

let indexPromise: Promise<SearchEntry[]> | null = null

export function loadIndex(): Promise<SearchEntry[]> {
  if (!indexPromise) {
    indexPromise = fetch(contentUrl('search.json'), { cache: 'no-cache' }).then((r) => {
      if (!r.ok) throw new Error(`search index: ${r.status}`)
      return r.json() as Promise<SearchEntry[]>
    })
  }
  return indexPromise
}

function snippetAround(text: string, term: string, width = 70): string {
  const lower = text.toLowerCase()
  const at = lower.indexOf(term)
  if (at < 0) return text.slice(0, width * 2) + (text.length > width * 2 ? '…' : '')
  const start = Math.max(0, at - width)
  const end = Math.min(text.length, at + term.length + width)
  return (start > 0 ? '…' : '') + text.slice(start, end) + (end < text.length ? '…' : '')
}

/** Every term must appear somewhere; titles and headings score higher than body text. */
export function search(index: SearchEntry[], query: string, limit = 12): SearchHit[] {
  const terms = query.toLowerCase().split(/\s+/).filter(Boolean)
  if (terms.length === 0) return []
  const hits: SearchHit[] = []
  for (const entry of index) {
    const title = entry.title.toLowerCase()
    const headings = entry.headings.join(' ').toLowerCase()
    const text = entry.text.toLowerCase()
    let score = 0
    let ok = true
    for (const term of terms) {
      let s = 0
      if (title.includes(term)) s += 10
      if (headings.includes(term)) s += 4
      if (text.includes(term)) {
        s += 1
        // small bonus for repeated mentions, capped
        let count = 0
        let i = text.indexOf(term)
        while (i >= 0 && count < 5) {
          count++
          i = text.indexOf(term, i + term.length)
        }
        s += count * 0.2
      }
      if (s === 0) {
        ok = false
        break
      }
      score += s
    }
    if (!ok) continue
    if (entry.kind === 'page') score += 1 // prefer lessons over problems on ties
    hits.push({ entry, score, snippet: snippetAround(entry.text, terms[0]) })
  }
  hits.sort((a, b) => b.score - a.score || a.entry.title.localeCompare(b.entry.title))
  return hits.slice(0, limit)
}
