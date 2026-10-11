# Everything but the first

Write `rest(items)` that returns a new list with everything except the
first item. For an empty list return an empty list.

```static
rest(["apple", "bread", "milk"])  ->  ["bread", "milk"]
rest([])                          ->  []
```

## Starter

```python
def rest(items):
    ...
```

## Hints

1. A slice from position 1.
2. `items[1:]`

## Approach

Slicing past the end of an empty list gives an empty list, so no special case is needed.

## Reference

```python
def rest(items):
    return items[1:]
```
