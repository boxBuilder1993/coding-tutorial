import type { ReactNode } from 'react'
import ReactMarkdown, { type Components } from 'react-markdown'
import remarkGfm from 'remark-gfm'
import type { Problem } from '../lib/content'
import { problemHref, resolveSiteLink } from '../lib/router'
import { PlayBlock } from './PlayBlock'
import { ExerciseCard } from './ExerciseCard'

const DIRECTIVE = /^:::problem\s+([a-z0-9][a-z0-9-]*)\s*$/

interface Props {
  source: string
  pagePath: string
  problems?: Record<string, Problem>
  /** Render ```python fences as runnable play blocks (default true). */
  runnable?: boolean
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function hastText(node: any): string {
  if (!node) return ''
  if (node.type === 'text') return node.value ?? ''
  return (node.children ?? []).map(hastText).join('')
}

function makeComponents(pagePath: string, runnable: boolean): Components {
  return {
    pre({ node }) {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const codeEl = (node as any)?.children?.find((c: any) => c.type === 'element' && c.tagName === 'code')
      const classes: string[] = codeEl?.properties?.className ?? []
      const lang = classes.find((c) => c.startsWith('language-'))?.slice('language-'.length) ?? ''
      const meta: string = codeEl?.data?.meta ?? ''
      const text = hastText(codeEl).replace(/\n$/, '')
      if (runnable && lang === 'python' && !/\bstatic\b/.test(meta)) {
        return <PlayBlock code={text} />
      }
      return (
        <pre className={`static ${lang ? 'lang-' + lang : ''}`}>
          <code>{text}</code>
        </pre>
      )
    },
    a({ href, children }) {
      const h = href ?? ''
      if (h.startsWith('problem:')) {
        return <a href={problemHref(h.slice('problem:'.length))}>{children}</a>
      }
      const internal = resolveSiteLink(h, pagePath)
      if (internal) return <a href={internal}>{children}</a>
      const external = /^https?:/i.test(h)
      return (
        <a href={h} target={external ? '_blank' : undefined} rel={external ? 'noreferrer' : undefined}>
          {children}
        </a>
      )
    },
  }
}

/** Markdown with runnable python fences and `:::problem id` exercise cards. */
export function Markdown({ source, pagePath, problems = {}, runnable = true }: Props) {
  const components = makeComponents(pagePath, runnable)
  const parts: ReactNode[] = []
  let buffer: string[] = []
  const flush = () => {
    if (buffer.length === 0) return
    parts.push(
      <ReactMarkdown key={parts.length} remarkPlugins={[remarkGfm]} components={components}>
        {buffer.join('\n')}
      </ReactMarkdown>,
    )
    buffer = []
  }
  for (const line of source.split('\n')) {
    const m = DIRECTIVE.exec(line)
    if (m) {
      flush()
      const p = problems[m[1]]
      parts.push(
        p ? (
          <ExerciseCard key={parts.length} problem={p} layout="stacked" />
        ) : (
          <div key={parts.length} className="error-summary">
            Unknown problem “{m[1]}”.
          </div>
        ),
      )
    } else {
      buffer.push(line)
    }
  }
  flush()
  return <div className="markdown">{parts}</div>
}
