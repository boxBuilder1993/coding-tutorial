# Binary search

When a list is already sorted, you can find a value without looking at
every item. Keep two positions, `low` and `high`, marking the
part of the list that could still contain the target; at first that is the
whole list. Look at the middle item. If it equals the target, you are done.
If it is smaller than the target, the target can only be to the right, so
move `low` to just after the middle. If it is larger, move `high` to just
before the middle. Repeat until the two positions cross, which means the
target is not there.

Write `binary_search(sorted_items, target)` that returns the position of
`target` in a sorted list, or `-1`.

```static
binary_search([2, 5, 8, 12, 16, 23], 12)  ->  3
binary_search([2, 5, 8], 6)               ->  -1
```

## Starter

```python
def binary_search(sorted_items, target):
    ...
```

## Hints

1. `low, high = 0, len(sorted_items) - 1` and loop `while low <= high`.
2. `mid = (low + high) // 2`; compare `sorted_items[mid]` with the target to move `low` or `high`.

## Approach

Each round halves the range. The loop condition `low <= high` means "there is still at least one candidate position".

## Reference

```python
def binary_search(sorted_items, target):
    low = 0
    high = len(sorted_items) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            return mid
        if sorted_items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
