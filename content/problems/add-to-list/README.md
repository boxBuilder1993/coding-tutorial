# Add to the list

Write `add_item(items, item)` that adds `item` to the end of the list
`items` and returns the list.

```static
add_item(["apple"], "bread")  ->  ["apple", "bread"]
add_item([], "milk")          ->  ["milk"]
```

## Starter

```python
def add_item(items, item):
    ...
```

## Hints

1. `append` adds to the end, and changes the list in place.
2. `append` returns `None`, so call it on its own line and then `return items`.

## Approach

Two lines: `items.append(item)`, then `return items`. Writing `return items.append(item)` returns `None`.

## Reference

```python
def add_item(items, item):
    items.append(item)
    return items
```
