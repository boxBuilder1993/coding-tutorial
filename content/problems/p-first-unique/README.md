# First unique item

Write `first_unique(items)` that returns the first item that appears
exactly once in the list, or `None` if every item repeats.

```static
first_unique(["milk", "bread", "milk", "eggs"])  ->  "bread"
first_unique(["a", "a"])                         ->  None
```

## Starter

```python
def first_unique(items):
    ...
```

## Hints

1. Count everything first, then walk the list again looking for a count of 1.
2. Two passes: a counting dictionary, then `for item in items: if counts[item] == 1: return item`.

## Approach

Order matters, so a second pass over the original list finds the first with count 1.

## Reference

```python
def first_unique(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    for item in items:
        if counts[item] == 1:
            return item
    return None
```
