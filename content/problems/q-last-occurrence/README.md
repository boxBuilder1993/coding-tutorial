# Last occurrence

Write `last_occurrence(items, target)` that returns the index of the last `target`
in a sorted list that may contain repeats, or `-1` if it is absent.

```static
last_occurrence([1, 2, 2, 2, 3, 5], 2)  ->  3
last_occurrence([1, 2, 2, 2, 3, 5], 4)  ->  -1
```

The point is to practise binary search that keeps going right after a match.

## Starter

```python
def last_occurrence(items, target):
    ...
```

## Hints

1. On a match, record `mid` and set `low = mid + 1` to keep looking to the right.
2. Return the recorded index after the loop, or `-1`.

## Approach

The mirror image of first occurrence: a match moves `low` past it instead of `high` before it. The last recorded match is the answer.

## Reference

```python
def last_occurrence(items, target):
    low, high = 0, len(items) - 1
    found = -1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            found = mid
            low = mid + 1
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return found
```
