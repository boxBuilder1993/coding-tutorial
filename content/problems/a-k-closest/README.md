# k closest to the shop

`points` is a list of `(x, y)` coordinates and the shop is at `(0, 0)`.
Write `k_closest(points, k)` that returns the `k` points nearest the shop,
ordered from nearest to farthest. No two points in the checks are at the
same distance.

```static
k_closest([(3, 3), (5, -1), (-2, 4)], 2)  ->  [(3, 3), (-2, 4)]
k_closest([(1, 3), (-2, 2)], 1)           ->  [(-2, 2)]
```

The point is to practise a heap of tuples keyed by a computed value.
Compare squared distances, `x * x + y * y`, and skip the square root.

## Starter

```python
def k_closest(points, k):
    ...
```

## Hints

1. Build tuples `(x * x + y * y, (x, y))` so the heap orders by distance.
2. `heapq.nsmallest(k, ...)` on those tuples, then strip the distance off each.
3. Or push each tuple into a max-heap of size `k` by negating the distance, then sort what remains.

## Approach

Pair each point with its squared distance so tuple comparison sorts by distance, take the `k` smallest with `nsmallest`, and return just the points. Squared distance orders the same way as true distance and avoids floats.

## Reference

```python
import heapq

def k_closest(points, k):
    keyed = [(x * x + y * y, (x, y)) for x, y in points]
    return [p for d, p in heapq.nsmallest(k, keyed)]
```
