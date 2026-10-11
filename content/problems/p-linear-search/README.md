# Linear search

The simplest way to find something in a list is to look at each item in
turn, from the first to the last, and stop as soon as you see what you are
looking for. If you reach the end without seeing it, it is not there.

Write `linear_search(items, target)` that returns the position of the first
item equal to `target`, or `-1` if there is none. The point is to write the
loop yourself rather than call the `index` method or test `target in items`.

```static
linear_search(["milk", "bread", "eggs"], "bread")  ->  1
linear_search(["milk"], "eggs")                    ->  -1
```

## Starter

```python
def linear_search(items, target):
    ...
```

## Hints

1. `for i in range(len(items))` and return inside the loop on a match.
2. The `-1` goes after the loop, so it is only reached when nothing matched.

## Approach

Return from inside the loop at the first match; the fall-through return handles the not-found case.

## Reference

```python
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
```
