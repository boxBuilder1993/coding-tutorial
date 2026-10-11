# Free delivery?

Delivery is free for orders of 50 or more. Write `is_free_delivery(total)`
that returns `True` when delivery is free and `False` otherwise.

```static
is_free_delivery(60)  ->  True
is_free_delivery(50)  ->  True
is_free_delivery(49)  ->  False
```

## Starter

```python
def is_free_delivery(total):
    ...
```

## Hints

1. The page's `is_in_stock` returned `quantity > 0` with no `if`. Which comparison says "50 or more"?
2. `return total >= 50`. The comparison already gives `True` or `False`.

## Approach

`return total >= 50`. No `if` is needed.

## Reference

```python
def is_free_delivery(total):
    return total >= 50
```
