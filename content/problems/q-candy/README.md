# Sweets by rating

Children stand in a line with `ratings`. Each child gets at least one sweet, and any child
with a higher rating than a neighbour must get more sweets than that neighbour. Write
`min_sweets(ratings)` that returns the fewest sweets in total.

```static
min_sweets([1, 0, 2])  ->  5     (2, 1, 2)
min_sweets([1, 2, 2])  ->  4     (1, 2, 1)
min_sweets([5])        ->  1
```

The point is to practise a two-pass greedy: satisfy the left neighbours going right, then
the right neighbours going left, taking the max.

## Starter

```python
def min_sweets(ratings):
    ...
```

## Hints

1. Start everyone at 1. Left to right: if `ratings[i] > ratings[i - 1]`, `sweets[i] = sweets[i - 1] + 1`.
2. Right to left: if `ratings[i] > ratings[i + 1]`, `sweets[i] = max(sweets[i], sweets[i + 1] + 1)`.
3. Sum.

## Approach

Each pass handles one direction of constraint; taking the maximum in the second pass keeps the first pass's constraints satisfied. Two linear passes.

## Reference

```python
def min_sweets(ratings):
    n = len(ratings)
    sweets = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            sweets[i] = sweets[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            sweets[i] = max(sweets[i], sweets[i + 1] + 1)
    return sum(sweets)
```
