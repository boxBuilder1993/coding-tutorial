# Discounted total

Orders of 100 or more get 20% off, orders of 50 or more get 10% off, smaller
orders pay full price. Write `to_pay(total)` that returns the amount to pay,
rounded to two decimal places.

```static
to_pay(120)  ->  96.0
to_pay(60)   ->  54.0
to_pay(20)   ->  20
```

## Starter

```python
def to_pay(total):
    ...
```

## Hints

1. `if` / `elif` / `else` to pick a rate, then arithmetic.
2. `round(total * (1 - rate), 2)`

## Approach

Pick the rate with the largest threshold first, then apply it.

## Reference

```python
def to_pay(total):
    if total >= 100:
        rate = 0.2
    elif total >= 50:
        rate = 0.1
    else:
        rate = 0
    return round(total * (1 - rate), 2)
```
