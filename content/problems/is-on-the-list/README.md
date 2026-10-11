# Is it on the list?

Write `on_list(items, item)` that returns `True` if `item` is one of the
values in `items`, and `False` otherwise.

```static
on_list(["apple", "bread"], "bread")  ->  True
on_list(["apple", "bread"], "milk")   ->  False
```

## Starter

```python
def on_list(items, item):
    ...
```

## Hints

1. `in` works on lists just like strings.
2. `return item in items`

## Approach

The `in` operator gives the boolean directly.

## Reference

```python
def on_list(items, item):
    return item in items
```
