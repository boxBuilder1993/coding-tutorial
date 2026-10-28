# k most frequent numbers

Write `k_frequent(nums, k)` that returns the `k` values that appear most often, most
frequent first; when two values tie, the smaller comes first. `k` is at most the number
of distinct values.

```static
k_frequent([1, 1, 1, 2, 2, 3], 2)  ->  [1, 2]
k_frequent([4, 4, 5, 5, 6], 2)     ->  [4, 5]
```

The point is to practise a heap keyed on `(-count, value)`.

## Starter

```python
def k_frequent(nums, k):
    ...
```

## Hints

1. Count with a `Counter`.
2. `heapq.nsmallest(k, counts, key=lambda v: (-counts[v], v))` orders by count descending then value ascending.

## Approach

Count, then select `k` with a two-part key. `nsmallest` with a key does the heap work.

## Reference

```python
import heapq
from collections import Counter

def k_frequent(nums, k):
    counts = Counter(nums)
    return heapq.nsmallest(k, counts, key=lambda v: (-counts[v], v))
```
