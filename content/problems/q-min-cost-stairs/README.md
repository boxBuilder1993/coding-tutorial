# Cheapest way up the stairs

`cost` lists the price of stepping on each stair. You may start on stair 0 or stair 1 and
climb one or two stairs at a time; you finish when you step past the last stair. Write
`min_cost(cost)` that returns the cheapest total.

```static
min_cost([10, 15, 20])                        ->  15
min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])  ->  6
```

The point is to practise a DP whose subproblem is "cheapest way to reach stair i".

## Starter

```python
def min_cost(cost):
    ...
```

## Hints

1. `reach[i]` = cheapest total to stand on stair `i` = `cost[i] + min(reach[i - 1], reach[i - 2])`, with `reach[0] = cost[0]`, `reach[1] = cost[1]`.
2. The answer is `min` of the last two, since you can finish from either.

## Approach

Each stair is reached from one of the two below it. Two running variables suffice. Linear.

## Reference

```python
def min_cost(cost):
    a, b = cost[0], cost[1]
    for c in cost[2:]:
        a, b = b, c + min(a, b)
    return min(a, b)
```
