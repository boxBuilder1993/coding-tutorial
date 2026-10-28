# Insert position

Write `insert_position(items, target)` that returns the index at which
`target` should be inserted into the sorted list `items` to keep it
sorted. If `target` is already present, return the index of its first
occurrence. This is what `bisect.bisect_left` does; write it yourself.

```static
insert_position([1, 3, 5, 7], 4)  ->  2
insert_position([1, 3, 5, 7], 5)  ->  2
insert_position([1, 3, 5, 7], 9)  ->  4
insert_position([], 9)            ->  0
```

The point is to practise binary search for a boundary rather than a
match: the answer is the first index whose item is at least `target`.

## Starter

```python
def insert_position(items, target):
    ...
```

## Hints

1. Think of it as "the first index `i` where `items[i] >= target`", which is `len(items)` if there is none.
2. Use `low, high = 0, len(items)` (note: not `len - 1`). While `low < high`: if `items[mid] < target`, `low = mid + 1`, else `high = mid`.
3. When the loop ends `low == high`, and that is the answer.

## Approach

A half-open binary search. `low` is the first index that might still be the answer, `high` is one past the last. Items smaller than the target push `low` past them; items at least the target pull `high` down to them (not past them, since `mid` itself could be the answer). They meet at the boundary.

## Reference

```python
def insert_position(items, target):
    low, high = 0, len(items)
    while low < high:
        mid = (low + high) // 2
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low
```
