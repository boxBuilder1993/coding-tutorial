# Restock until full

Deliveries arrive in boxes of `box` loaves. Write `deliveries_needed(stock, box, target)`
that returns how many boxes must be added before `stock` reaches at least
`target`. If stock already meets the target, return 0.

```static
deliveries_needed(2, 3, 10)   ->  3     (2 -> 5 -> 8 -> 11)
deliveries_needed(10, 3, 10)  ->  0
```

## Starter

```python
def deliveries_needed(stock, box, target):
    boxes = 0
    while ...:
        ...
    return boxes
```

## Hints

1. Keep going while `stock < target`.
2. Each round: add a box to stock and add one to the count.

## Approach

A `while` with two updates in the body. Both are needed: forgetting `stock += box` is an infinite loop.

## Reference

```python
def deliveries_needed(stock, box, target):
    boxes = 0
    while stock < target:
        stock += box
        boxes += 1
    return boxes
```
