# All in stock

Write `all_in_stock(quantities)` that returns `True` if every quantity in
the list is greater than zero, and `False` if any is zero or negative. An
empty list counts as all in stock.

```static
all_in_stock([3, 1, 5])  ->  True
all_in_stock([3, 0, 5])  ->  False
all_in_stock([])         ->  True
```

The point is to practise `all` with a loop inside the brackets.

## Starter

```python
def all_in_stock(quantities):
    ...
```

## Hints

1. `all(... for q in quantities)` with a condition on `q` in the gap.
2. The condition is `q > 0`.

## Approach

One line: `return all(q > 0 for q in quantities)`. `all` of an empty list is `True`, which matches the rule for empty input.

## Reference

```python
def all_in_stock(quantities):
    return all(q > 0 for q in quantities)
```
