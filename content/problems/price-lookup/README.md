# Price lookup

Write `price_of(prices, item)` that returns the price stored for `item` in
the dictionary `prices`, or `0` if the item is not listed.

```static
price_of({"apple": 40, "bread": 25}, "bread")  ->  25
price_of({"apple": 40, "bread": 25}, "milk")   ->  0
```

## Starter

```python
def price_of(prices, item):
    ...
```

## Hints

1. `prices[item]` fails with a `KeyError` when the item is missing.
2. `get` takes a default: `prices.get(item, 0)`.

## Approach

`return prices.get(item, 0)`. An `if item in prices` check followed by indexing is the long form.

## Reference

```python
def price_of(prices, item):
    return prices.get(item, 0)
```
