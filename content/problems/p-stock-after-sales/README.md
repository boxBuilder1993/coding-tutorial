# Stock after sales

`stock` maps items to quantities and `sales` is a list of item names, one
per item sold. Write `after_sales(stock, sales)` that reduces each sold
item's quantity by one, changing `stock` itself, and returns it. Every sold
item is in stock.

```static
after_sales({"apple": 3, "bread": 2}, ["apple", "bread", "apple"])  ->  {"apple": 1, "bread": 1}
```

## Starter

```python
def after_sales(stock, sales):
    ...
```

## Hints

1. A loop over `sales` that updates the dictionary.
2. `stock[item] -= 1`

## Approach

Each sale is one decrement of the matching key.

## Reference

```python
def after_sales(stock, sales):
    for item in sales:
        stock[item] -= 1
    return stock
```
