# Steps to find

Write `steps_to_find(items, target)` that searches `items` from the start
and returns how many items it looked at, counting the one it found. If
`target` is not there, every item was looked at, so return the length.

```static
steps_to_find([3, 5, 7], 7)   ->  3
steps_to_find([3, 5, 7], 3)   ->  1
steps_to_find([3, 5, 7], 9)   ->  3
steps_to_find([], 9)          ->  0
```

The best case is one step, the worst is `len(items)`. When we say a search
is "linear", it is the worst case we mean.

## Starter

```python
def steps_to_find(items, target):
    ...
```

## Hints

1. Loop with a counter that goes up by one for each item, and return it as soon as the item matches.
2. If the loop finishes without returning, the target was absent: return the counter, which now equals `len(items)`.

## Approach

A single loop with a counter. Return inside the loop on a match, and after the loop otherwise.

## Reference

```python
def steps_to_find(items, target):
    steps = 0
    for item in items:
        steps += 1
        if item == target:
            return steps
    return steps
```
