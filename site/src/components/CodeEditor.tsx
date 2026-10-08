import { useEffect, useRef } from 'react'
import { EditorState, Prec } from '@codemirror/state'
import { EditorView, keymap } from '@codemirror/view'
import { indentWithTab } from '@codemirror/commands'
import { indentUnit } from '@codemirror/language'
import { python } from '@codemirror/lang-python'
import { basicSetup } from 'codemirror'

interface Props {
  value: string
  onChange: (value: string) => void
  onRun?: () => void
  minLines?: number
  ariaLabel?: string
}

export function CodeEditor({ value, onChange, onRun, minLines = 4, ariaLabel }: Props) {
  const host = useRef<HTMLDivElement>(null)
  const view = useRef<EditorView | null>(null)
  const onChangeRef = useRef(onChange)
  const onRunRef = useRef(onRun)
  onChangeRef.current = onChange
  onRunRef.current = onRun

  useEffect(() => {
    if (!host.current) return
    const runKey = Prec.highest(
      keymap.of([
        {
          key: 'Mod-Enter',
          run: () => {
            onRunRef.current?.()
            return true
          },
        },
      ]),
    )
    const state = EditorState.create({
      doc: value,
      extensions: [
        basicSetup,
        python(),
        indentUnit.of('    '),
        keymap.of([indentWithTab]),
        runKey,
        EditorView.updateListener.of((u) => {
          if (u.docChanged) onChangeRef.current(u.state.doc.toString())
        }),
        EditorView.theme({
          '&': { fontSize: '14px' },
          '.cm-content': { minHeight: `${minLines * 1.5}em`, fontFamily: 'var(--mono)' },
          '.cm-gutters': { fontFamily: 'var(--mono)' },
        }),
      ],
    })
    view.current = new EditorView({ state, parent: host.current })
    if (ariaLabel) view.current.contentDOM.setAttribute('aria-label', ariaLabel)
    return () => {
      view.current?.destroy()
      view.current = null
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  // Sync external value changes (reset to starter) without clobbering typing.
  useEffect(() => {
    const v = view.current
    if (!v) return
    const current = v.state.doc.toString()
    if (current !== value) {
      v.dispatch({ changes: { from: 0, to: current.length, insert: value } })
    }
  }, [value])

  return <div className="editor" ref={host} />
}
