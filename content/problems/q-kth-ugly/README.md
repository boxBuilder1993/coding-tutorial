# k-th number with only small factors

A "smooth" number here is a positive whole number whose only prime factors are 2, 3 or 5:
`1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...`. Write `kth_smooth(k)` that returns the `k`-th one.

```static
kth_smooth(1)   ->  1
kth_smooth(7)   ->  8
kth_smooth(10)  ->  12
```

The point is to practise generating values in order with a heap and a set to avoid
repeats: each popped number spawns three candidates.

## Starter

```python
def kth_smooth(k):
    ...
```

## Hints

1. Heap starting with `[1]` and a `seen` set with `{1}`.
2. Pop `k` times; for the popped `x`, push `2x`, `3x`, `5x` if not already seen. The `k`-th pop is the answer.

## Approach

A heap always yields the smallest unprocessed candidate, and the set stops `6` arriving as both `2 * 3` and `3 * 2`. About k log k.

## Reference

```python
import heapq

def kth_smooth(k):
    heap = [1]
    seen = {1}
    for _ in range(k):
        x = heapq.heappop(heap)
        for m in (2, 3, 5):
            if x * m not in seen:
                seen.add(x * m)
                heapq.heappush(heap, x * m)
    return x
```
