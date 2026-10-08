# Delivery fee

Delivery costs 5, but it is free for orders of 50 or more. Write
`delivery_fee(total)` that returns the fee.

```static
delivery_fee(60)  ->  0
delivery_fee(50)  ->  0
delivery_fee(20)  ->  5
```

## Starter

```python
def delivery_fee(total):
    ...
```

## Hints

1. `if total >= 50:` then return 0.
2. After the `if` block, `return 5` handles every other case.

## Approach

An `if` that returns early, then a plain `return` for the rest. `if`/`else` works just as well.

## Reference

```python
def delivery_fee(total):
    if total >= 50:
        return 0
    return 5
```
