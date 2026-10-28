# k-th smallest across sorted lists

`lists` is a list of sorted lists. Write `kth_smallest(lists, k)` that returns the `k`-th
smallest value across all of them, counting repeats, with `k = 1` the smallest. `k` is at
most the total count.

```static
kth_smallest([[1, 5, 9], [2, 3], [4]], 4)  ->  4
kth_smallest([[1, 1], [1]], 3)             ->  1
```

The point is to practise the k-way merge with a heap, stopping after `k` pops.

## Starter

```python
def kth_smallest(lists, k):
    ...
```

## Hints

1. Heap of `(value, list_index, position)` for the head of each non-empty list.
2. Pop `k` times; after each pop push the next item from the same list if there is one. The `k`-th popped value is the answer.

## Approach

Merge k sorted lists with a heap, but stop after `k` items. Cost k log(number of lists). Flattening and sorting also passes but does all the work.

## Reference

```python
import heapq

def kth_smallest(lists, k):
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    for _ in range(k):
        value, i, pos = heapq.heappop(heap)
        if pos + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][pos + 1], i, pos + 1))
    return value
```
