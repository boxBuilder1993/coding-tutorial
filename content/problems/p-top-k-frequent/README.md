# Top k most frequent

Find the `k` values that appear most often in a list. Count each value
with a dictionary, then pick the `k` entries with the largest counts.
`heapq.nlargest` can do the picking if you give it a `key` that reads the
count from each `(value, count)` pair.

Write `most_frequent(items, k)` that returns the `k` most frequent values
as a list, most frequent first. Ties are broken by the value itself in
ascending order. `k` never exceeds the number of distinct values.

```static
most_frequent(["a", "b", "a", "c", "b", "a"], 2)  ->  ["a", "b"]
most_frequent([3, 1, 3, 1, 2], 2)                 ->  [1, 3]
```

## Starter

```python
import heapq

def most_frequent(items, k):
    ...
```

## Hints

1. Count with `get(item, 0) + 1`. Then rank the `(value, count)` pairs.
2. `sorted(counts.items(), key=lambda p: (-p[1], p[0]))[:k]` or `heapq.nsmallest(k, counts.items(), key=lambda p: (-p[1], p[0]))`, then take the values.

## Approach

Two steps: a counting pass, then a ranking by `(-count, value)` so bigger counts come first and ties go by value.

## Reference

```python
import heapq

def most_frequent(items, k):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    top = heapq.nsmallest(k, counts.items(), key=lambda p: (-p[1], p[0]))
    return [value for value, count in top]
```
