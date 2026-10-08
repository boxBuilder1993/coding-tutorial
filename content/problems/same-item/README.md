# Same item?

Write `same_item(a, b)` that returns `True` if the two item names are the
same, ignoring whether letters are capitals or not.

```static
same_item("bread", "bread")  ->  True
same_item("Bread", "bread")  ->  True
same_item("bread", "milk")   ->  False
```

You can turn a string into all lowercase with `.lower()`, like `a.lower()`.
Methods get a full page later; for now, use that one.

## Starter

```python
def same_item(a, b):
    ...
```

## Hints

1. Compare the lowercase versions of both with `==`.
2. `return a.lower() == b.lower()`

## Approach

Normalise both sides to lowercase, then compare for equality.

## Reference

```python
def same_item(a, b):
    return a.lower() == b.lower()
```
