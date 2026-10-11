# Apply a price change

Write `set_price(prices, item, price)` that stores `price` under `item` in
the dictionary you are given, adding the item if it is new or replacing the
old price, and returns that same dictionary. Do not build a new one.

```static
set_price({"apple": 40}, "bread", 25)  ->  {"apple": 40, "bread": 25}
set_price({"apple": 40}, "apple", 45)  ->  {"apple": 45}
```

## Starter

```python
def set_price(prices, item, price):
    ...
```

## Hints

1. Assigning to a key adds or replaces: `prices[item] = price`.
2. Then `return prices`.

## Approach

One assignment and a return. The same line handles both the new and the existing key.

## Reference

```python
def set_price(prices, item, price):
    prices[item] = price
    return prices
```
