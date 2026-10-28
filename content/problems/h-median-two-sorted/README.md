# Median of two sorted lists

Write `median(a, b)` that returns the median of all values in two sorted lists combined
(the middle value, or the average of the two middles), as a float. At least one list is
non-empty.

```static
median([1, 3], [2])     ->  2.0
median([1, 2], [3, 4])  ->  2.5
median([], [1])         ->  1.0
```

Merging is linear and passes. The interview answer binary-searches how many items of the
shorter list belong in the left half, which is logarithmic; try it once the merge works.

## Starter

```python
def median(a, b):
    ...
```

## Hints

1. Merge version: walk both with two indices until you have produced the middle one or two values.
2. Binary-search version: on the shorter list, choose `i` items for the left half and `j = half - i` from the other; adjust `i` until `a[i-1] <= b[j]` and `b[j-1] <= a[i]`, treating missing ends as infinities.

## Approach

Either produce the middle by merging (linear) or find the partition point by binary search on the shorter list (logarithmic). Both are exact.

## Reference

```python
def median(a, b):
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    half = (m + n + 1) // 2
    low, high = 0, m
    INF = float("inf")
    while low <= high:
        i = (low + high) // 2
        j = half - i
        a_left = a[i - 1] if i > 0 else -INF
        a_right = a[i] if i < m else INF
        b_left = b[j - 1] if j > 0 else -INF
        b_right = b[j] if j < n else INF
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            high = i - 1
        else:
            low = i + 1
```
