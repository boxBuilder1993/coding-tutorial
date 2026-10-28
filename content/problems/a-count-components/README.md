# Count the groups

`graph` is an adjacency dictionary for a two-way graph; every node is a
key, including nodes with no neighbours. Write `count_components(graph)`
that returns how many separate connected groups there are.

```static
count_components({1: [2], 2: [1], 3: [4], 4: [3, 5], 5: [4], 6: []})  ->  3
count_components({})                                                  ->  0
```

The point is to practise running a search from every unvisited node.

## Starter

```python
def count_components(graph):
    ...
```

## Hints

1. A `visited` set and a counter. Loop over every node in `graph`; skip visited ones.
2. For each unvisited node, add one to the counter and explore everything reachable from it (stack or queue), marking visited.
3. Return the counter.

## Approach

Each search from a fresh node marks one whole component. The outer loop guarantees every node is reached eventually; the visited set guarantees each component is counted once. Linear in nodes plus edges.

## Reference

```python
def count_components(graph):
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
```
