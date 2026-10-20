# Has a duplicate, fast

Write `has_duplicate(items)` that returns `True` if any value appears in
`items` more than once, and `False` otherwise.

```static
has_duplicate([1, 2, 3, 2])  ->  True
has_duplicate([1, 2, 3])     ->  False
has_duplicate([])            ->  False
```

The point is to practise doing this in one pass. One of the checks hands
you sixty thousand items. Comparing every pair is nearly two billion steps
and will not finish inside the ten-second limit; a set makes it one loop.

## Starter

```python
def has_duplicate(items):
    ...
```

## Hints

1. Keep a set of values seen so far. For each item, check the set before adding to it.
2. `item in seen` on a set is one step, however big the set is. Return `True` the moment it is found.
3. Alternative: a list has a duplicate exactly when `len(set(items)) < len(items)`.

## Approach

Loop once. If the item is already in the `seen` set, return `True`; otherwise add it. After the loop, return `False`. Both lookups and additions on a set are constant time, so the whole thing is linear.

## Reference

```python
def has_duplicate(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False
```
