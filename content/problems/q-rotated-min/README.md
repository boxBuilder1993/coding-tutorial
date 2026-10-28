# Smallest in a rotated list

A sorted list of distinct numbers was rotated: some number of items were moved from the
front to the back, so `[1, 2, 4, 7, 9]` might have become `[7, 9, 1, 2, 4]`. Write
`rotated_min(items)` that returns the smallest value.

```static
rotated_min([7, 9, 1, 2, 4])  ->  1
rotated_min([1, 2, 4, 7, 9])  ->  1     (rotated by zero)
rotated_min([3])              ->  3
```

The point is to practise binary search on a list that is sorted in two pieces.

## Starter

```python
def rotated_min(items):
    ...
```

## Hints

1. Compare `items[mid]` with `items[high]`. If `mid` is bigger, the minimum is to the right of `mid`.
2. Otherwise the minimum is at `mid` or to its left: `high = mid`. Stop when `low == high`.

## Approach

The right end tells you which piece `mid` is in. A middle larger than the right end means the drop happens after `mid`; otherwise the drop is at or before `mid`. Logarithmic.

## Reference

```python
def rotated_min(items):
    low, high = 0, len(items) - 1
    while low < high:
        mid = (low + high) // 2
        if items[mid] > items[high]:
            low = mid + 1
        else:
            high = mid
    return items[low]
```
