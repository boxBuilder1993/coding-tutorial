# Sum, recursively

Write `total(items)` that returns the sum of a list of numbers, using
recursion: the total of a list is its first item plus the total of the
rest, and the total of an empty list is `0`.

```static
total([3, 5, 7])  ->  15
total([])         ->  0
```

The point is to practise recursion, so write it without a loop and without
`sum`.

## Starter

```python
def total(items):
    ...
```

## Hints

1. Base case first: `if not items: return 0`.
2. `items[0]` is the first item and `items[1:]` is the rest. Add the first to `total` of the rest.

## Approach

Two lines after the base case: `return items[0] + total(items[1:])`. Each call handles one item and hands the rest down.

## Reference

```python
def total(items):
    if not items:
        return 0
    return items[0] + total(items[1:])
```
