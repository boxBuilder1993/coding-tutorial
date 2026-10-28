# Sort a nearly sorted list

Every item in `items` is at most `k` positions away from where it belongs in sorted
order. Write `sort_nearly(items, k)` that returns the sorted list.

```static
sort_nearly([6, 5, 3, 2, 8, 10, 9], 3)  ->  [2, 3, 5, 6, 8, 9, 10]
sort_nearly([1, 2, 3], 0)               ->  [1, 2, 3]
```

The point is to practise a heap of size `k + 1`: the smallest of the next `k + 1` items
must be the next item of the output. `sorted` also passes; the heap version is n log k.

## Starter

```python
def sort_nearly(items, k):
    ...
```

## Hints

1. Push the first `k + 1` items into a heap.
2. For each remaining item: pop the smallest to the output, push the item. Then drain the heap.

## Approach

With displacement bounded by `k`, the global minimum is always among the first `k + 1` unsorted items, so a small heap suffices. n log k.

## Reference

```python
import heapq

def sort_nearly(items, k):
    heap = list(items[:k + 1])
    heapq.heapify(heap)
    out = []
    for x in items[k + 1:]:
        out.append(heapq.heappushpop(heap, x))
    while heap:
        out.append(heapq.heappop(heap))
    return out
```
