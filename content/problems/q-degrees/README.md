# Count each node's connections

Write `degrees(edges)` that, for a two-way graph given as a list of `(a, b)` pairs,
returns a dictionary from each node to how many edges touch it.

```static
degrees([("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")])  ->  {"A": 2, "B": 2, "C": 3, "D": 1}
degrees([])  ->  {}
```

The point is to practise reading an edge list with a Counter.

## Starter

```python
def degrees(edges):
    ...
```

## Hints

1. Each edge adds one to both of its nodes.
2. A `Counter` makes the increments one line each; return `dict(counter)`.

## Approach

One pass over the edges incrementing two counts each. Linear in the number of edges.

## Reference

```python
from collections import Counter

def degrees(edges):
    counts = Counter()
    for a, b in edges:
        counts[a] += 1
        counts[b] += 1
    return dict(counts)
```
