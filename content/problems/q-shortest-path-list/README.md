# The shortest route itself

Write `shortest_path(graph, start, goal)` that returns the list of nodes on a shortest
route from `start` to `goal` in a two-way graph, including both ends, or `[]` if there is
none. When several shortest routes exist, return the one BFS finds when neighbours are
explored in the order they are listed.

```static
graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"]}
shortest_path(graph, "A", "E")  ->  ["A", "B", "D", "E"]
shortest_path(graph, "A", "A")  ->  ["A"]
shortest_path({"A": [], "B": []}, "A", "B")  ->  []
```

The point is to practise recording predecessors during BFS and walking them back.

## Starter

```python
def shortest_path(graph, start, goal):
    ...
```

## Hints

1. `parent = {start: None}` doubles as the visited set. When you first reach a neighbour, record `parent[nb] = node`.
2. Stop when `goal` is reached. Then follow `parent` from `goal` back to `start`, collecting nodes, and reverse.

## Approach

BFS with a parent map; the first time a node is reached is along a shortest route, so the chain of parents is a shortest path. Linear.

## Reference

```python
from collections import deque

def shortest_path(graph, start, goal):
    parent = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            break
        for nb in graph[node]:
            if nb not in parent:
                parent[nb] = node
                queue.append(nb)
    if goal not in parent:
        return []
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]
```
