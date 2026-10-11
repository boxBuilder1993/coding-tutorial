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

1. Which of the two numbers do you take away from which?
2. `return paid - cost`. Order matters: `cost - paid` gives a negative answer.

## Approach

`return paid - cost`.

## Reference

```python
def change_due(paid, cost):
    return paid - cost
```
