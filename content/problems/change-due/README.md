# Change due

Write a function `change_due(paid, cost)` that returns how much change a
customer should get back.

```static
change_due(50, 35)  ->  15
change_due(20, 20)  ->  0
```

## Starter

```python
def change_due(paid, cost):
    ...
```

## Hints

1. Change is what was paid minus what it cost.
2. Order matters: `paid - cost`, not `cost - paid`.

## Approach

`return paid - cost`.

## Reference

```python
def change_due(paid, cost):
    return paid - cost
```
