# First occurrence

Write `first_occurrence(items, target)` that returns the index of the
first `target` in a sorted list that may contain repeats, or `-1` if it is
absent.

```static
first_occurrence([1, 2, 2, 2, 3, 5], 2)  ->  1
first_occurrence([1, 2, 2, 2, 3, 5], 4)  ->  -1
first_occurrence([], 4)                  ->  -1
```

The point is to practise binary search that keeps going after a match.
One check uses a list of a million items, where a linear scan is slow but
still passes; the shape is what matters here.

## Starter

```python
def first_occurrence(items, target):
    ...
```

## Hints

1. Standard `low`, `high`, `mid` loop. On a match, record `mid` and set `high = mid - 1` to keep looking left.
2. Return the recorded index after the loop, or `-1` if nothing was recorded.

## Approach

Binary search where a match does not stop the loop. Save `mid` in `found` and move `high` left of it; smaller items move `low` right; larger move `high` left. The last `found` is the first occurrence.

## Reference

```python
def first_occurrence(items, target):
    low, high = 0, len(items) - 1
    found = -1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            found = mid
            high = mid - 1
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return found
```
