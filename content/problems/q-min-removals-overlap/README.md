# Fewest removals to end overlaps

`intervals` is a list of `(start, end)` pairs; two touching at an endpoint do not overlap.
Write `min_removals(intervals)` that returns the fewest intervals to remove so none of
the remaining ones overlap.

```static
min_removals([(1, 2), (2, 3), (3, 4), (1, 3)])  ->  1
min_removals([(1, 2), (1, 2), (1, 2)])          ->  2
min_removals([(1, 2), (2, 3)])                  ->  0
```

The point is to practise seeing a problem as the complement of one you know: keep the
most non-overlapping intervals (earliest end first), remove the rest.

## Starter

```python
def min_removals(intervals):
    ...
```

## Hints

1. Sort by end. Count how many you can keep with the earliest-end rule.
2. Answer is `len(intervals) - kept`.

## Approach

Maximum non-overlapping set by earliest end, then subtract. n log n.

## Reference

```python
def min_removals(intervals):
    kept = 0
    last_end = float("-inf")
    for start, end in sorted(intervals, key=lambda iv: iv[1]):
        if start >= last_end:
            kept += 1
            last_end = end
    return len(intervals) - kept
```
