# Search a rotated list

A sorted list of distinct numbers has been rotated, as in the previous problem. Write
`search_rotated(items, target)` that returns the index of `target`, or `-1`.

```static
search_rotated([4, 5, 6, 7, 0, 1, 2], 0)  ->  4
search_rotated([4, 5, 6, 7, 0, 1, 2], 3)  ->  -1
```

The point is to practise working out which half is sorted and whether the target lies in it.

## Starter

```python
def search_rotated(items, target):
    ...
```

## Hints

1. At each step one of the two halves, `low..mid` or `mid..high`, is properly sorted. `items[low] <= items[mid]` tells you it is the left one.
2. If the sorted half contains the target (compare with its two ends), search it; otherwise search the other half.

## Approach

Standard binary search with an extra question: which side is sorted, and is the target within that side's range? One of the two halves is always sorted, and a range check on a sorted half is reliable. Logarithmic.

## Reference

```python
def search_rotated(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[low] <= items[mid]:
            if items[low] <= target < items[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if items[mid] < target <= items[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
```
