export interface TreeNode {
  path: string
  title: string
  problems: string[]
  links: string[]
  children: TreeNode[]
}

export interface Problem {
  id: string
  title: string
  statement: string
  starter: string
  hints: string[]
  approach: string
  reference: string
}

export interface Content {
  tree: TreeNode
  problems: Record<string, Problem>
}

export const BASE = import.meta.env.BASE_URL.endsWith('/') ? import.meta.env.BASE_URL : import.meta.env.BASE_URL + '/'

export function contentUrl(rel: string): string {
  return `${BASE}content/${rel}`
}

async function fetchText(url: string): Promise<string> {
  const res = await fetch(url, { cache: 'no-cache' })
  if (!res.ok) throw new Error(`${res.status} ${res.statusText} for ${url}`)
  return res.text()
}

export async function loadContent(): Promise<Content> {
  const [tree, problems] = await Promise.all([
    fetchText(contentUrl('tree.json')).then((t) => JSON.parse(t) as TreeNode),
    fetchText(contentUrl('problems.json')).then((t) => JSON.parse(t) as Record<string, Problem>),
  ])
  return { tree, problems }
}

const mdCache = new Map<string, Promise<string>>()
export function fetchPage(path: string): Promise<string> {
  const rel = path ? `site/${path}/README.md` : 'site/README.md'
  if (!mdCache.has(rel)) mdCache.set(rel, fetchText(contentUrl(rel)))
  return mdCache.get(rel)!
}

const checkCache = new Map<string, Promise<string>>()
export function fetchCheck(id: string): Promise<string> {
  if (!checkCache.has(id)) checkCache.set(id, fetchText(contentUrl(`problems/${id}/check.py`)))
  return checkCache.get(id)!
}

export function* walkTree(node: TreeNode): Generator<TreeNode> {
  yield node
  for (const c of node.children) yield* walkTree(c)
}

export function findNode(tree: TreeNode, path: string): TreeNode | undefined {
  for (const n of walkTree(tree)) if (n.path === path) return n
  return undefined
}

/** Strip a leading "# Title" line; used where the title is shown separately. */
export function stripTitle(markdown: string): string {
  return markdown.replace(/^#\s+[^\n]*\n+/, '')
}
