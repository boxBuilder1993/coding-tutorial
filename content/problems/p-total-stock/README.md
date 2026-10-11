# Total stock

`stock` maps item names to quantities. Write `total_stock(stock)` that
returns the sum of all the quantities.

```static
total_stock({"apple": 10, "bread": 3})  ->  13
total_stock({})                         ->  0
```

## Starter

```python
def total_stock(stock):
    ...
```

## Hints

1. `values()` and `sum`.
2. `sum(stock.values())`

## Approach

`values()` gives just the quantities; `sum` adds them.

## Reference

```python
def total_stock(stock):
    return sum(stock.values())
```
