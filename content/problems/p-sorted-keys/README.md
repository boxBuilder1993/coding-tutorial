# Items in order

`prices` maps item names to prices. Write `item_names(prices)` that returns
the item names as a list in alphabetical order.

```static
item_names({"milk": 2.5, "apple": 40, "bread": 25})  ->  ["apple", "bread", "milk"]
```

## Starter

```python
def item_names(prices):
    ...
```

## Hints

1. `sorted` works on a dictionary's keys directly.
2. `sorted(prices)`

## Approach

Looping over a dict gives keys, so `sorted(prices)` sorts the keys. `sorted(prices.keys())` is the same.

## Reference

```python
def item_names(prices):
    return sorted(prices)
```
