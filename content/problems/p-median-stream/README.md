# Median price

Write `median(prices)` that returns the median of a non-empty list: the
middle value when sorted, or the average of the two middle values when the
count is even. Do not change the list you are given.

```static
median([40, 2.5, 25])      ->  25
median([40, 2.5, 25, 10])  ->  17.5
```

## Starter

```python
def median(prices):
    ...
```

## Hints

1. `sorted`, then index by `len // 2`, with a branch for even length.
2. Even: average of positions `n // 2 - 1` and `n // 2`.

## Approach

Sort a copy, then one `if` on `len(prices) % 2`.

## Reference

```python
def median(prices):
    s = sorted(prices)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2
```
