# Pairs that make a price

Write `pairs_summing(prices, target)` that returns how many pairs of
positions `(i, j)` with `i < j` have `prices[i] + prices[j] == target`.

```static
pairs_summing([10, 30, 20, 30], 40)  ->  2     (10+30 at positions 0,1 and 0,3)
pairs_summing([5], 10)               ->  0
```

## Starter

```python
def pairs_summing(prices, target):
    ...
```

## Hints

1. Two nested loops, the inner one starting after the outer.
2. `for i in range(len(prices)): for j in range(i + 1, len(prices)):`

## Approach

Nested loops with `j` starting at `i + 1` so each pair is counted once and an element is never paired with itself.

## Reference

```python
def pairs_summing(prices, target):
    count = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] == target:
                count += 1
    return count
```
