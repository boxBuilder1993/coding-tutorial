# Shortest distances with weights

`graph` is a dictionary from each node to a list of `(neighbour, weight)` pairs with
non-negative weights; every node is a key. Write `distances(graph, source)` that returns a
dictionary from every reachable node to its shortest total distance from `source`.

```static
graph = {"A": [("B", 4), ("C", 1)], "B": [("D", 1)], "C": [("B", 2), ("D", 5)], "D": []}
distances(graph, "A")  ->  {"A": 0, "B": 3, "C": 1, "D": 4}
```

This is Dijkstra's algorithm: breadth-first search with the queue replaced by a heap of
`(distance, node)`, so the closest unsettled node is always processed next.

## Starter

```python
def distances(graph, source):
    ...
```

## Hints

1. `dist = {source: 0}`, heap `[(0, source)]`. Pop the smallest; if its distance is larger than the recorded one, skip it (stale entry).
2. For each `(nb, w)`, if `dist[node] + w` improves `dist.get(nb, inf)`, record it and push `(new, nb)`.
3. Non-negative weights are what make 'settle the closest first' correct.

## Approach

A heap orders candidates by tentative distance; the first time a node is popped its distance is final. Stale heap entries are skipped rather than removed. (V + E) log V.

## Reference

```python
import heapq

def distances(graph, source):
    dist = {source: 0}
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float("inf")):
            continue
        for nb, w in graph[node]:
            nd = d + w
            if nd < dist.get(nb, float("inf")):
                dist[nb] = nd
                heapq.heappush(heap, (nd, nb))
    return dist
```
