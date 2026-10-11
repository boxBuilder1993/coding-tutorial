# Count the items

Write `count_items(basket)` that returns a dictionary mapping each item in
the list `basket` to how many times it appears.

```static
count_items(["apple", "bread", "apple"])  ->  {"apple": 2, "bread": 1}
count_items([])                           ->  {}
```

## Starter

```python
def count_items(basket):
    counts = {}
    for item in basket:
        ...
    return counts
```

## Hints

1. For each item, look up its current count with a default of 0, add one, and store it back.
2. `counts[item] = counts.get(item, 0) + 1`

## Approach

The counting pattern from the page. `get` with a default avoids a separate "is it there yet" check.

## Reference

```python
def count_items(basket):
    counts = {}
    for item in basket:
        counts[item] = counts.get(item, 0) + 1
    return counts
```
