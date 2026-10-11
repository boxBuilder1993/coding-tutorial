# Second cheapest

Write `second_cheapest(prices)` that returns the second smallest number in
a list of at least two different numbers.

```static
second_cheapest([40, 2.5, 25])  ->  25
```

## Starter

```python
def second_cheapest(prices):
    ...
```

## Hints

1. Sort a copy, then index.
2. `sorted(prices)[1]`

## Approach

`sorted` returns a new ascending list; position 1 is the second smallest.

## Reference

```python
def second_cheapest(prices):
    return sorted(prices)[1]
```
