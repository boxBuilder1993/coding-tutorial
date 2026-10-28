# Does the network contain a loop?

`graph` is an adjacency dictionary for a two-way graph with every node as a key and no
edge listed twice. Write `has_cycle(graph)` that returns whether any cycle exists.

```static
has_cycle({1: [2], 2: [1, 3], 3: [2]})           ->  False     (a line)
has_cycle({1: [2, 3], 2: [1, 3], 3: [1, 2]})     ->  True      (a triangle)
has_cycle({1: [2], 2: [1], 3: [4], 4: [3]})      ->  False
```

The point is to practise DFS that remembers where it came from: in an undirected graph,
seeing a visited neighbour that is not your parent means a cycle.

## Starter

```python
def has_cycle(graph):
    ...
```

## Hints

1. DFS from each unvisited node, passing the parent along.
2. For each neighbour: unvisited means recurse; visited and not the parent means a cycle.
3. Alternative: a connected component with `n` nodes and at least `n` edges has a cycle.

## Approach

Depth-first search with a parent parameter so the edge you arrived by is not mistaken for a loop. Linear in nodes plus edges.

## Reference

```python
def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nb in graph[node]:
            if nb not in visited:
                if dfs(nb, node):
                    return True
            elif nb != parent:
                return True
        return False

    for start in graph:
        if start not in visited and dfs(start, None):
            return True
    return False
```
