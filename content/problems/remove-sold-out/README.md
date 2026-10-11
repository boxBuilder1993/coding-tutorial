# Remove a sold-out item

Write `remove_item(items, item)` that removes `item` from the list if it is
there, and leaves the list alone if it is not. If `item` appears more than
once, remove only the first one. Change the list itself and return it.

```static
remove_item(["apple", "bread", "milk"], "bread")  ->  ["apple", "milk"]
remove_item(["apple", "milk"], "eggs")            ->  ["apple", "milk"]
remove_item(["a", "b", "a"], "a")                 ->  ["b", "a"]
```

## Starter

```python
def remove_item(items, item):
    ...
```

## Hints

1. `remove` raises an error when the value is absent, so check with `in` first.
2. `if item in items:` then `items.remove(item)`.

## Approach

Guard the `remove` with an `in` check, then return the list either way.

## Reference

```python
def remove_item(items, item):
    if item in items:
        items.remove(item)
    return items
```
