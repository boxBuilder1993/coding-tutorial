# Reverse in place

To reverse a list without making a new one, keep one position at the
front and one at the back. Swap the two items, then move the front position
one step right and the back one step left. Stop when they meet or cross.

Write `reverse_in_place(items)` that reverses the list in place using this
method and returns it. Do not use slicing, `reverse` or `reversed`.

```static
reverse_in_place([1, 2, 3, 4])  ->  [4, 3, 2, 1]
```

## Starter

```python
def reverse_in_place(items):
    ...
```

## Hints

1. `left, right = 0, len(items) - 1` and loop `while left < right`.
2. Swap, then `left += 1` and `right -= 1`.

## Approach

Two pointers closing in. For odd lengths the middle item stays put without special handling.

## Reference

```python
def reverse_in_place(items):
    left = 0
    right = len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items
```
