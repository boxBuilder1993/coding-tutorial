# Valid quantity?

A customer can order between 1 and 20 of an item. Write
`is_valid_quantity(q)` that returns `True` if `q` is in that range, inclusive,
and `False` otherwise.

```static
is_valid_quantity(1)   ->  True
is_valid_quantity(20)  ->  True
is_valid_quantity(0)   ->  False
is_valid_quantity(21)  ->  False
```

## Starter

```python
def is_valid_quantity(q):
    ...
```

## Hints

1. Two conditions must both hold. Combine them with `and`.
2. `q >= 1 and q <= 20`

## Approach

Return the combined comparison. Python also allows the chained form `1 <= q <= 20`, which reads like maths.

## Reference

```python
def is_valid_quantity(q):
    return q >= 1 and q <= 20
```
