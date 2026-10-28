# Closest value in a sorted list

Write `closest(items, target)` that returns the value in the non-empty sorted list
`items` closest to `target`. If two values are equally close, return the smaller.

```static
closest([1, 4, 6, 9], 5)   ->  4
closest([1, 4, 6, 9], 7)   ->  6
closest([1, 4, 6, 9], 100) ->  9
```

The point is to practise using the insertion position: the answer is one of the two
values either side of where `target` would go.

## Starter

```python
def closest(items, target):
    ...
```

## Hints

1. Find `i`, the first index with `items[i] >= target` (by hand or `bisect.bisect_left`).
2. The candidates are `items[i - 1]` and `items[i]`, where they exist. Pick the closer, preferring the smaller on a tie.

## Approach

One boundary search, then compare at most two candidates. Logarithmic.

## Reference

```python
import bisect

def closest(items, target):
    i = bisect.bisect_left(items, target)
    candidates = []
    if i > 0:
        candidates.append(items[i - 1])
    if i < len(items):
        candidates.append(items[i])
    return min(candidates, key=lambda v: (abs(v - target), v))
```
