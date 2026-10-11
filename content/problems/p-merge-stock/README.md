# Merge two stock counts

Two shops report stock as dictionaries from item to quantity. Write
`merged(a, b)` that returns one dictionary with the quantities added
together for items in either.

```static
merged({"apple": 3, "bread": 2}, {"bread": 1, "milk": 5})  ->  {"apple": 3, "bread": 3, "milk": 5}
```

## Starter

```python
def merged(a, b):
    ...
```

## Hints

1. Start from a copy of one, then add the other in with `get`.
2. `result[item] = result.get(item, 0) + qty`

## Approach

Copy `a` with `dict(a)` so the input is not changed, then fold `b` in with the counting pattern.

## Reference

```python
def merged(a, b):
    result = dict(a)
    for item, qty in b.items():
        result[item] = result.get(item, 0) + qty
    return result
```
