# Is there a path?

`graph` is an adjacency dictionary for a **directed** graph: an entry
`"A": ["B"]` means you can go from `A` to `B` but not necessarily back.
Every node is a key. Write `path_exists(graph, start, goal)` that returns
whether `goal` can be reached from `start` by following edges. A node can
reach itself.

```static
graph = {"A": ["B"], "B": ["C"], "C": [], "D": ["A"]}
path_exists(graph, "A", "C")  ->  True
path_exists(graph, "C", "A")  ->  False
path_exists(graph, "D", "C")  ->  True
```

The point is to practise depth-first search with a visited set on a graph
that may contain cycles.

## Starter

```python
def path_exists(graph, start, goal):
    ...
```

## Hints

1. Recursive DFS: `def visit(node)` that returns `True` if `node == goal`, marks it visited, and returns `True` if any unvisited neighbour's `visit` does.
2. Or iterative: a stack starting with `start`; pop, check for goal, push unvisited neighbours.
3. Without the visited set a cycle loops forever.

## Approach

Any search works since only reachability matters. The visited set makes each node processed once, so the search is linear and terminates on cyclic graphs.

## Reference

```python
def path_exists(graph, start, goal):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node == goal:
            return True
        if node in visited:
            continue
        visited.add(node)
        stack.extend(graph[node])
    return False
```
