# First true

`flags` is a list of booleans that is `False` for a while and then `True` for the rest,
like `[False, False, True, True]`. Either part may be empty. Write `first_true(flags)`
that returns the index of the first `True`, or `len(flags)` if there is none.

```static
first_true([False, False, True, True])  ->  2
first_true([True])                      ->  0
first_true([False, False])              ->  2
```

The point is to practise the boundary form of binary search, which is the template for
every "search on an answer" problem.

## Starter

```python
def first_true(flags):
    ...
```

## Hints

1. `low, high = 0, len(flags)`; while `low < high`: if `flags[mid]` is `True`, `high = mid`, else `low = mid + 1`.
2. Return `low`.

## Approach

Half-open binary search for a boundary. A `True` at `mid` means the boundary is at or before `mid`; a `False` means it is after. `low` ends at the first `True`, or at `len` when there is none.

## Reference

```python
def first_true(flags):
    low, high = 0, len(flags)
    while low < high:
        mid = (low + high) // 2
        if flags[mid]:
            high = mid
        else:
            low = mid + 1
    return low
```
