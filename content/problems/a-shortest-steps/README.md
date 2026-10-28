# Shortest number of steps

`graph` is an adjacency dictionary for a two-way graph; every node is a
key. Write `shortest_steps(graph, start, goal)` that returns the fewest
edges on any route from `start` to `goal`, or `-1` if there is no route.
`start` and `goal` may be the same node, in which case the answer is `0`.

```static
graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C", "E"], "E": ["D"], "F": []}
shortest_steps(graph, "A", "E")  ->  3
shortest_steps(graph, "A", "F")  ->  -1
shortest_steps(graph, "A", "A")  ->  0
```

The point is to practise breadth-first search with a distance dictionary.

## Starter

```python
def shortest_steps(graph, start, goal):
    ...
```

## Hints

1. `distance = {start: 0}` and a `deque([start])`.
2. Pop a node; for each neighbour not yet in `distance`, record `distance[node] + 1` and queue it.
3. Return `distance.get(goal, -1)`, or return early as soon as `goal` is reached.

## Approach

BFS reaches nodes in order of distance, so the first time `goal` is recorded its distance is the shortest. The dictionary doubles as the visited set.

## Reference

```python
from collections import deque

def shortest_steps(graph, start, goal):
    distance = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            return distance[node]
        for neighbour in graph[node]:
            if neighbour not in distance:
                distance[neighbour] = distance[node] + 1
                queue.append(neighbour)
    return -1
```
