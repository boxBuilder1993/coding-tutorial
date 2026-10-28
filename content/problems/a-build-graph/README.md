# Build the adjacency list

Write `build_graph(edges)` that turns a list of `(a, b)` pairs describing
two-way connections into a dictionary from each node to a **sorted** list
of its neighbours. Every node that appears in any edge must be a key.

```static
build_graph([("A", "B"), ("A", "C"), ("C", "B")])
    ->  {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
build_graph([])  ->  {}
```

The point is to practise the adjacency-list representation.

## Starter

```python
def build_graph(edges):
    ...
```

## Hints

1. For each edge add `b` to `a`'s list and `a` to `b`'s list, creating lists as needed with `setdefault` or a `defaultdict(list)`.
2. Sort each neighbour list at the end, and return a plain `dict`.

## Approach

One pass over the edges adding both directions, then one pass over the keys to sort the lists. Returning `dict(graph)` makes a `defaultdict` compare equal to the expected dictionary.

## Reference

```python
def build_graph(edges):
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    for node in graph:
        graph[node].sort()
    return graph
```
