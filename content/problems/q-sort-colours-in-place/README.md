# Sort three colours in place

`items` contains only `0`, `1` and `2`. Write `sort_colours(items)` that rearranges
the list **in place** so all `0`s come first, then `1`s, then `2`s. Return nothing; the
checks look at the list afterwards.

```static
items = [2, 0, 2, 1, 1, 0];  sort_colours(items)  ->  items is now [0, 0, 1, 1, 2, 2]
```

The point is to practise sorting without `sorted`: count the three values and overwrite,
or use three pointers (the Dutch national flag method) for a single pass.

## Starter

```python
def sort_colours(items):
    ...
```

## Hints

1. Counting version: count zeros, ones and twos; then write them back with index assignment, `items[i] = ...`.
2. One-pass version: `low`, `mid`, `high` pointers; swap a `0` at `mid` to `low`, a `2` at `mid` to `high`, step past a `1`.
3. Do not do `items = sorted(items)`: that rebinds the name and leaves the caller's list unchanged.

## Approach

Either two linear passes (count, then overwrite) or one pass with three pointers. Both are linear and modify the list the caller holds.

## Reference

```python
def sort_colours(items):
    low, mid, high = 0, 0, len(items) - 1
    while mid <= high:
        if items[mid] == 0:
            items[low], items[mid] = items[mid], items[low]
            low += 1
            mid += 1
        elif items[mid] == 2:
            items[mid], items[high] = items[high], items[mid]
            high -= 1
        else:
            mid += 1
```
