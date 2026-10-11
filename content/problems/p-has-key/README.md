# Is it priced?

Write `is_priced(prices, item)` that returns `True` if `item` is a key in
the dictionary `prices`.

```static
is_priced({"apple": 40}, "apple")  ->  True
is_priced({"apple": 40}, "milk")   ->  False
```

## Starter

```python
def is_priced(prices, item):
    ...
```

## Hints

1. `in` on a dictionary checks keys.
2. `return item in prices`

## Approach

`in` tests for a key directly; no need to look at the values.

## Reference

```python
def is_priced(prices, item):
    return item in prices
```
