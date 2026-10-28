# Pick the largest k times

`piles` is a list of positive whole numbers. You make `k` picks; each pick takes the
largest pile's current value as your score and then halves that pile, rounding up. Write
`max_score(piles, k)` that returns the total score.

```static
max_score([10, 10, 10, 10, 10], 5)  ->  50
max_score([1, 10, 3, 3, 3], 3)      ->  18     (10, then 5, then 3)
```

The point is to practise a heap where popped items go back changed.

## Starter

```python
def max_score(piles, k):
    ...
```

## Hints

1. Max-heap by negation. `k` times: pop the largest, add it to the score, push back `(value + 1) // 2`.
2. `(x + 1) // 2` is the ceiling of `x / 2` for whole numbers.

## Approach

Each pick is a pop and a push, log n each; `k` picks. Sorting once does not work because the halved pile may still be the largest.

## Reference

```python
import heapq

def max_score(piles, k):
    heap = [-p for p in piles]
    heapq.heapify(heap)
    score = 0
    for _ in range(k):
        top = -heapq.heappop(heap)
        score += top
        heapq.heappush(heap, -((top + 1) // 2))
    return score
```
