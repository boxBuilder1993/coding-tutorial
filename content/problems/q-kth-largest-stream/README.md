# k-th largest after each arrival

Write `kth_largest_stream(nums, k)` that returns a list with, for each position `i`, the
`k`-th largest value among `nums[0..i]`, or `None` when fewer than `k` values have
arrived.

```static
kth_largest_stream([4, 5, 8, 2], 3)  ->  [None, None, 4, 4]
kth_largest_stream([3, 1], 1)        ->  [3, 3]
```

The point is to practise maintaining a heap of size `k` across a stream.

## Starter

```python
def kth_largest_stream(nums, k):
    ...
```

## Hints

1. Min-heap of at most `k` items. Push each value; if the heap exceeds `k`, pop the smallest.
2. When the heap has `k` items, its root is the current `k`-th largest.

## Approach

The heap holds the `k` largest seen so far and its root is the smallest of them. Each arrival costs log k.

## Reference

```python
import heapq

def kth_largest_stream(nums, k):
    heap = []
    out = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
        out.append(heap[0] if len(heap) == k else None)
    return out
```
