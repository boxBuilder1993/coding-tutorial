# Discount rate

The shop gives a discount based on quantity: 10 or more items get 20%,
5 to 9 items get 10%, fewer than 5 get nothing. Write `discount_rate(quantity)`
that returns the rate as a number: `0.2`, `0.1`, or `0`.

```static
discount_rate(12)  ->  0.2
discount_rate(5)   ->  0.1
discount_rate(2)   ->  0
```

## Starter

```python
def discount_rate(quantity):
    ...
```

## Hints

1. Check the biggest threshold first, then the next, with `if` / `elif` / `else`.
2. If you check `>= 5` before `>= 10`, large orders get the small discount.

## Approach

Three branches from largest to smallest. Order matters because the first true condition wins.

## Reference

```python
def discount_rate(quantity):
    if quantity >= 10:
        return 0.2
    elif quantity >= 5:
        return 0.1
    else:
        return 0
```
