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

1. A comparison already gives `True` or `False`. Return it directly.
2. "50 or more" is `total >= 50`.

## Approach

`return total >= 50`. No `if` is needed.

## Reference

```python
def is_free_delivery(total):
    return total >= 50
```
