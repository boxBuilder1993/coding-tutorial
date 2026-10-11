# Last item

Write `last_item(items)` that returns the last value in the list `items`.
The list always has at least one item.

```static
last_item(["apple", "bread", "milk"])  ->  "milk"
last_item([7])                         ->  7
```

## Starter

```python
def last_item(items):
    ...
```

## Hints

1. Negative positions count from the end.
2. `items[-1]`

## Approach

Index `-1`. `items[len(items) - 1]` is the same thing, longer.

## Reference

```python
def last_item(items):
    return items[-1]
```
