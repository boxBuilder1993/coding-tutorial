import type { Problem } from './content'
import { cleanTraceback, summarize } from './errors'
import type { TestResult } from '../runner/runner'

const RULES = `You are a strict but kind programming tutor. Your student is learning Python and is working on the exercise below. Your job is to help them solve it THEMSELVES. Follow these rules without exception:

1. Never write code that solves the problem, in full or in part. Not even "just the loop". If asked for the answer, refuse and offer a smaller question instead.
2. Do not say what the bug is. Help the student find it by asking them to trace their code by hand on a failing input.
3. One question or one nudge per reply, in two to four sentences.
4. Name the Python concept involved (for example "slicing" or "dictionary get with a default") and tell the student to type that word into the search box on the site to reread the lesson. Do not explain the concept yourself.
5. If the student explains their reasoning, respond to the reasoning, not to the code.
6. Once the checks pass, ask the student to explain their solution in two sentences, then point out one thing that could be simpler, as a question.`

/** Markdown statement to plain text: drop the title, fences markers and inline backticks. */
function plainStatement(md: string): string {
  return md
    .replace(/^#\s+[^\n]*\n+/, '')
    .replace(/^```[^\n]*$/gm, '')
    .replace(/`/g, '')
    .replace(/\n{3,}/g, '\n\n')
    .trim()
}

export function buildTutorPrompt(problem: Problem, code: string, result: TestResult | null, hintsRevealed: string[]): string {
  let opening: string
  let results: string

  if (!result) {
    opening = 'Start by asking the student what they think the problem is asking and how they would approach it, in their own words. Wait for their answer before saying anything else.'
    results = 'The student has not run the checks yet.'
  } else if (result.status === 'pass') {
    opening = 'The code passes every check. Start by asking the student to explain in two sentences why it works. Then ask one question about anything that could be simpler.'
    results = result.cases.map((c) => `PASS  ${c.name}`).join('\n')
  } else {
    opening = 'Start by asking the student why they think their code is not working, in their own words. Wait for their answer before saying anything else.'
    const lines: string[] = []
    if (result.status === 'timeout') lines.push('The run was stopped after 10 seconds: the code did not finish.')
    if (result.status === 'missing') {
      lines.push(result.missingName ? `The checks could not find a definition named "${result.missingName}" in the student's code.` : 'The checks could not import what they need from the student\'s code.')
    }
    if (result.status === 'not-attempted') lines.push('The code still raises NotImplementedError.')
    for (const c of result.cases) {
      if (c.status === 'pass') lines.push(`PASS  ${c.name}`)
      else if (c.status === 'fail') lines.push(`FAIL  ${c.name}\n      expected: ${c.expected}\n      got:      ${c.actual}${c.message ? `\n      note: ${c.message}` : ''}`)
      else lines.push(`ERROR ${c.name}${c.message ? `: ${c.message}` : ''}`)
    }
    if (result.error && result.status !== 'missing') {
      const clean = cleanTraceback(result.error)
      lines.push('', `Error summary: ${summarize(clean)}`, 'Traceback:', clean)
    }
    results = lines.join('\n')
  }

  const hints = hintsRevealed.length ? hintsRevealed.map((h, i) => `${i + 1}. ${h.replace(/`/g, '')}`).join('\n') : 'none'

  return [
    RULES,
    '',
    opening,
    '',
    '=== The exercise ===',
    problem.title,
    '',
    plainStatement(problem.statement),
    '',
    "=== The student's current code ===",
    code.trimEnd() || '(empty)',
    '',
    "=== Results of the student's last run ===",
    results,
    '',
    '=== Hints the student has already seen ===',
    hints,
    '',
  ].join('\n')
}
