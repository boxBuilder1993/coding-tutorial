/** Turn a Python traceback into a one-line, beginner-friendly summary. */

const USER_FILES = ['main.py', 'solution.py', 'check.py']

export function cleanTraceback(tb: string): string {
  const lines = tb.split('\n')
  const out: string[] = []
  let skipNext = false
  for (const line of lines) {
    if (skipNext) {
      skipNext = false
      if (!/^\s+File "/.test(line) && !/^\w*Error|^\w+:/.test(line)) continue
    }
    const m = /^\s+File "([^"]+)"/.exec(line)
    if (m && !USER_FILES.some((f) => m[1].endsWith(f))) {
      skipNext = true
      continue
    }
    out.push(line)
  }
  return out.join('\n').trim()
}

interface Located {
  file: string | null
  line: number | null
}

function locate(tb: string): Located {
  const matches = [...tb.matchAll(/File "([^"]+)", line (\d+)/g)]
  for (let i = matches.length - 1; i >= 0; i--) {
    const file = matches[i][1]
    if (USER_FILES.some((f) => file.endsWith(f))) {
      return { file: file.split('/').pop() ?? file, line: Number(matches[i][2]) }
    }
  }
  return { file: null, line: null }
}

export function summarize(tb: string): string {
  const lines = tb.trim().split('\n')
  const last = lines[lines.length - 1] ?? ''
  const m = /^([A-Za-z_][\w.]*)(?::\s*(.*))?$/.exec(last)
  const type = m?.[1] ?? 'Error'
  const msg = m?.[2] ?? last
  const { file, line } = locate(tb)
  const where = line ? ` (${file === 'check.py' ? 'in the tests, ' : ''}line ${line})` : ''

  switch (type) {
    case 'SyntaxError':
    case 'IndentationError':
    case 'TabError':
      return `Python could not read your code${where}: ${msg}.`
    case 'NameError': {
      const n = /name '([^']+)'/.exec(msg)?.[1]
      return n ? `You used \`${n}\` but never defined it${where}.` : `Unknown name${where}: ${msg}.`
    }
    case 'TypeError':
      return `A value of the wrong type was used${where}: ${msg}.`
    case 'ZeroDivisionError':
      return `Division by zero${where}.`
    case 'IndexError':
      return `A position is outside the list${where}: ${msg}.`
    case 'KeyError':
      return `Key ${msg} was not found in the dictionary${where}.`
    case 'AttributeError':
      return `${msg}${where}.`
    case 'RecursionError':
      return `Your code called itself too many times. Check the base case${where}.`
    case 'AssertionError':
      return `An assertion failed${where}${msg ? ': ' + msg : ''}.`
    default:
      return `${type}${msg ? ': ' + msg : ''}${where}.`
  }
}
