# Who stocks what

`shops` maps each shop name to a list of the items it stocks. Write
`stockists(shops)` that returns a dictionary from each item to the sorted
list of shops that stock it.

```static
stockists({"north": ["milk", "bread"], "south": ["bread"]})  ->  {"milk": ["north"], "bread": ["north", "south"]}
```

## Starter

```python
def stockists(shops):
    ...
```

## Hints

1. Nested loops over `items()` and each list, building lists in a dictionary.
2. After building, sort each list: `for item in result: result[item].sort()`.

## Approach

Invert a one-to-many mapping with the grouping pattern, then sort every group.

## Reference

```python
def stockists(shops):
    result = {}
    for shop, items in shops.items():
        for item in items:
            if item not in result:
                result[item] = []
            result[item].append(shop)
    for item in result:
        result[item].sort()
    return result
```
