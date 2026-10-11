# First duplicate

To find the first repeat, remember every value you have seen so far. Walk
the list; the first value that is already in your memory is the answer. A
set is the natural place to keep that memory.

Write `first_duplicate(items)` that returns the first item which has
appeared earlier in the list, or `None` if every item is different. "First"
means the item whose second appearance comes earliest, so for `[1, 2, 2, 1]`
the answer is `2`, not `1`.

```static
first_duplicate(["milk", "bread", "milk", "bread"])  ->  "milk"
first_duplicate([1, 2, 2, 1])                        ->  2
first_duplicate([1, 2, 3])                           ->  None
```

## Starter

```python
def first_duplicate(items):
    ...
```

## Hints

1. `seen = set()`; check `in seen` before adding.
2. Return as soon as the check succeeds; `None` after the loop.

## Approach

The seen-set pattern with an early return. Note the answer is the first item whose *second* appearance comes earliest, which is exactly what checking before adding gives.

## Reference

```python
def first_duplicate(items):
    seen = set()
    for item in items:
        if item in seen:
            return item
        seen.add(item)
    return None
```
