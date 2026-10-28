---
title: Graphs in Python: adjacency lists, BFS, DFS, shortest paths and grids
description: Adjacency lists, breadth-first and depth-first search, shortest paths by BFS, connected components, and grids treated as graphs.
---
# Graphs

A tree has one route from the root to anything. Drop that restriction,
let any node connect to any other, allow cycles, and you have a **graph**:
nodes (also called vertices) joined by edges. Cities and roads, people
and friendships, web pages and links, tasks and the order they must happen
in. Graph problems look intimidating and are mostly two loops you already
know.

## Representing a graph

The standard form is a dictionary from each node to the list of its
neighbours, the **adjacency list**. From a list of edges:

```python
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]

graph = {}
for a, b in edges:
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)
for node in sorted(graph):
    print(node, "->", graph[node])
```

Each edge is added in both directions because these roads go both ways;
an **undirected** graph. For a **directed** graph (follows, prerequisites,
one-way streets) add only `a -> b`. `setdefault` creates the empty list
the first time a node appears; `defaultdict(list)` does the same.

```static
    A --- B
    |     |
    C --- D --- E
```

## Breadth-first search

Starting at `A`, which nodes can be reached, and in how many steps? Same
queue loop as the tree's level order, with one addition: a graph can
loop back on itself, so keep a `visited` set and never queue a node
twice.

```python
from collections import deque

graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}

def bfs(graph, start):
    distance = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in distance:
                distance[neighbour] = distance[node] + 1
                queue.append(neighbour)
    return distance

print(bfs(graph, "A"))
```

The `distance` dictionary serves as the visited set, and because the
queue hands out nodes in order of distance, the first time a node is
reached is along a shortest route. That is the whole theory of
**shortest paths in an unweighted graph**: BFS, and read off the distance.
To recover the path itself, record each node's predecessor when you first
reach it and walk back from the target.

Every node is queued once and every edge looked at twice, so BFS is linear
in nodes plus edges.

## Depth-first search

DFS goes as deep as it can before backing up, which recursion does for
free. It visits the same nodes as BFS in a different order, and it is the
natural tool when the question is about *whether* something is reachable
or about structure (cycles, components, ordering) rather than about
distance.

```python
graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}

def dfs(graph, node, visited, order):
    visited.add(node)
    order.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, order)

visited = set()
order = []
dfs(graph, "A", visited, order)
print(order)
```

Mark the node visited **before** recursing into its neighbours, or a cycle
sends it round forever. For very large graphs the recursion depth can hit
Python's limit; the same traversal with an explicit stack (a list, `pop()`
from the end) has no such limit and is otherwise identical to BFS with the
queue swapped out.

## Connected components

How many separate groups are there? Run a search from every node not yet
visited; each run finds one component.

```python
graph = {1: [2], 2: [1], 3: [4], 4: [3, 5], 5: [4], 6: []}

def components(graph):
    visited = set()
    count = 0
    for start in graph:
        if start in visited:
            continue
        count += 1
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            stack.extend(graph[node])
    return count

print(components(graph))
```

This is DFS with a stack instead of recursion. Nodes may be pushed more
than once, which is why the visited check happens on pop. Friends
networks, islands on a map, and "which machines can reach each other"
are all this function.

## Grids are graphs

A grid of cells is a graph where each cell's neighbours are the cells
above, below, left and right. You never build the adjacency dictionary;
you compute neighbours from coordinates and check they are in bounds.

```python
grid = [
    "11000",
    "11000",
    "00100",
    "00011",
]

def count_islands(grid):
    rows, cols = len(grid), len(grid[0])
    seen = set()
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            islands += 1
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                if (cr, cc) in seen:
                    continue
                seen.add((cr, cc))
                for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        stack.append((nr, nc))
    return islands

print(count_islands(grid))
```

Cells are `(row, col)` tuples, which can go in a set because tuples are
hashable. The four-neighbour list and the bounds check are the only
grid-specific lines; everything else is the component count from above.
Shortest path through a maze is the same with BFS and a distance
dictionary.

## What is not here

Weighted shortest paths (Dijkstra's algorithm) are BFS with the queue
replaced by a priority queue from Module 4; topological ordering of tasks
with prerequisites is a DFS post-order reversed; both are good next
reads once this page is comfortable. The two searches on this page cover
most of what interviews ask about graphs.

## Try it

Graphs in the exercises arrive as an adjacency dictionary, or as a list of
edges for you to convert. Grids arrive as lists of strings.

:::problem a-build-graph

:::problem a-shortest-steps

:::problem a-count-components

:::problem a-path-exists

:::problem a-count-islands

Next: [Heaps revisited](../10-heaps-revisited).
