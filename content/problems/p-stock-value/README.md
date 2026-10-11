# Stock value

`stock` maps items to quantities and `prices` maps items to unit prices.
Write `stock_value(stock, prices)` that returns the total value of the
stock, counting only items that have a price.

```static
stock_value({"apple": 3, "bread": 2, "gift": 1}, {"apple": 40, "bread": 25})  ->  170
```

## Starter

```python
def stock_value(stock, prices):
    ...
```

## Hints

1. Loop over the stock, check `in prices`, multiply and add.
2. `if item in prices: total += qty * prices[item]`

## Approach

Two dictionaries joined by key, with `in` guarding the lookup.

## Reference

```python
def stock_value(stock, prices):
    total = 0
    for item, qty in stock.items():
        if item in prices:
            total += qty * prices[item]
    return total
```
