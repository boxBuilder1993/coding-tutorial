# Best profit with k trades

`prices` lists a stock's price each day. You may complete at most `k` buy-then-sell
transactions, never holding more than one share. Write `max_profit(prices, k)` that
returns the largest total profit.

```static
max_profit([2, 4, 1], 2)        ->  2
max_profit([3, 2, 6, 5, 0, 3], 2)  ->  7     (buy 2 sell 6, buy 0 sell 3)
max_profit([7, 6, 4, 3, 1], 1)  ->  0
```

State per transaction number: the best balance while holding and while not holding.
Update both for each day, from higher transaction counts down so a day is not used twice.

## Starter

```python
def max_profit(prices, k):
    ...
```

## Hints

1. If `k >= len(prices) // 2`, you can take every rise: sum the positive day-to-day differences.
2. Otherwise `hold[t]` (best while holding, having started transaction `t`) starts at `-inf`, `free[t]` at 0. For each price, for `t` from `k` down to 1: `hold[t] = max(hold[t], free[t - 1] - price)`; `free[t] = max(free[t], hold[t] + price)`.
3. Answer `free[k]`.

## Approach

A small state machine per transaction count, swept over the days. Days times k.

## Reference

```python
def max_profit(prices, k):
    if not prices or k == 0:
        return 0
    if k >= len(prices) // 2:
        return sum(max(0, b - a) for a, b in zip(prices, prices[1:]))
    hold = [float("-inf")] * (k + 1)
    free = [0] * (k + 1)
    for p in prices:
        for t in range(k, 0, -1):
            hold[t] = max(hold[t], free[t - 1] - p)
            free[t] = max(free[t], hold[t] + p)
    return free[k]
```
