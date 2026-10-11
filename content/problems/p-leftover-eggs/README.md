# Leftover eggs

Eggs are packed in boxes of `box_size`. Write `leftover(eggs, box_size)`
that returns how many eggs are left after packing as many full boxes as possible.

```static
leftover(20, 6)  ->  2
leftover(12, 6)  ->  0
```

## Starter

```python
def leftover(eggs, box_size):
    ...
```

## Hints

1. The remainder operator.
2. `eggs % box_size`

## Approach

`%` gives the remainder of the division.

## Reference

```python
def leftover(eggs, box_size):
    return eggs % box_size
```
