# Average price

Write `average(prices)` that returns the average of the numbers in `prices`,
rounded to 2 decimal places. The list has at least one number.

```static
average([40, 25, 2.5])  ->  22.5
average([1, 2])         ->  1.5
average([10, 20, 25])   ->  18.33
```

## Starter

```python
def average(prices):
    ...
```

## Hints

1. `sum(prices) / len(prices)` is the average.
2. `round(value, 2)` rounds to two decimal places.

## Approach

Three built-ins in one line: `round(sum(prices) / len(prices), 2)`.

## Reference

```python
def average(prices):
    return round(sum(prices) / len(prices), 2)
```
