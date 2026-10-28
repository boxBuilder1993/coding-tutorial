# Last stone standing

`stones` is a list of positive weights. Repeatedly take the two heaviest stones and smash
them together: if they are equal both are destroyed, otherwise the lighter is destroyed
and the heavier becomes the difference. Write `last_stone(stones)` that returns the
weight of the final stone, or `0` if none remain.

```static
last_stone([2, 7, 4, 1, 8, 1])  ->  1
last_stone([3, 3])              ->  0
last_stone([5])                 ->  5
```

The point is to practise simulating "take the two largest" with a max-heap via negation.

## Starter

```python
def last_stone(stones):
    ...
```

## Hints

1. Negate every weight, heapify. While at least two remain, pop two (the two largest).
2. If they differ, push the negated difference back. At the end return the remaining stone's weight or 0.

## Approach

A heap gives the two largest in log n each; `n - 1` smashes at most. Negation turns Python's min-heap into a max-heap.

## Reference

```python
import heapq

def last_stone(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0
```
