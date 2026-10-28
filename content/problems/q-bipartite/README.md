# Can the nodes be split into two teams?

Write `is_bipartite(graph)` that returns whether the nodes of the two-way graph can be
coloured with two colours so that no edge joins two nodes of the same colour. Every node
is a key.

```static
is_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})  ->  True     (a square)
is_bipartite({0: [1, 2], 1: [0, 2], 2: [0, 1]})             ->  False    (a triangle)
is_bipartite({})  ->  True
```

The point is to practise BFS that assigns alternating labels and checks for conflicts.

## Starter

```python
def is_bipartite(graph):
    ...
```

## Hints

1. `colour = {}`. For each uncoloured node, colour it 0 and BFS; each neighbour gets the opposite colour.
2. A neighbour that already has the same colour as the current node means it is impossible.

## Approach

Two-colouring by breadth-first search from every unvisited node. Any conflict means an odd cycle, which cannot be two-coloured. Linear.

## Reference

```python
from collections import deque

def is_bipartite(graph):
    colour = {}
    for start in graph:
        if start in colour:
            continue
        colour[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for nb in graph[node]:
                if nb not in colour:
                    colour[nb] = 1 - colour[node]
                    queue.append(nb)
                elif colour[nb] == colour[node]:
                    return False
    return True
```
