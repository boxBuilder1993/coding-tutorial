# Is the list empty?

Write `is_empty(items)` that returns `True` if the list has no items.

```static
is_empty([])         ->  True
is_empty(["bread"])  ->  False
```

## Starter

```python
def is_empty(items):
    ...
```

## Hints

1. `len` and a comparison.
2. `return len(items) == 0`

## Approach

Compare the length with 0. `return not items` also works, because an empty list counts as false.

## Reference

```python
def is_empty(items):
    return len(items) == 0
```
