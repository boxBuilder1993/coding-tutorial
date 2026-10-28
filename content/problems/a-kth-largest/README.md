# k-th largest

Write `kth_largest(nums, k)` that returns the k-th largest value in the
list, counting repeats as separate values (so in `[3, 3, 1]` the 2nd
largest is `3`). `k` is between 1 and `len(nums)`.

```static
kth_largest([3, 2, 1, 5, 6, 4], 2)        ->  5
kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)  ->  4
```

The point is to practise a heap bounded to size `k`. Sorting also passes;
try the heap.

## Starter

```python
def kth_largest(nums, k):
    ...
```

## Hints

1. Keep a min-heap of at most `k` items: push each number, and when the heap exceeds `k`, pop the smallest.
2. At the end the heap holds the `k` largest, and its root `heap[0]` is the smallest of those, which is the k-th largest.
3. `heapq.nlargest(k, nums)[-1]` is the one-line version.

## Approach

Push every number and keep popping the minimum while the heap has more than `k` items. The survivors are the top `k`; the root is the answer. Cost n log k.

## Reference

```python
import heapq

def kth_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```
