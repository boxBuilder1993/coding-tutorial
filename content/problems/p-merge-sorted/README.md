# Merge two sorted lists

If two lists are each already sorted, you can combine them into one sorted
list in a single pass. Keep a position in each list, both starting at the
front. Compare the two items at those positions, copy the smaller one to
the result and advance that list's position. When one list is used up, copy
the rest of the other.

Write `merge(a, b)` that returns a new sorted list containing everything
from both. Do not use `sort` or `sorted`.

```static
merge([1, 4, 9], [2, 3, 10])  ->  [1, 2, 3, 4, 9, 10]
merge([], [1, 2])             ->  [1, 2]
```

## Starter

```python
def merge(a, b):
    ...
```

## Hints

1. Two indices `i` and `j`, loop `while i < len(a) and j < len(b)`.
2. After the loop, `result.extend(a[i:])` and `result.extend(b[j:])`, or two more `while` loops.

## Approach

The two-pointer merge. Using `<=` when comparing keeps equal values from `a` before those from `b`.

## Reference

```python
def merge(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result
```
