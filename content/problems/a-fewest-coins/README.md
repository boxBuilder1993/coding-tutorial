# Fewest coins, any coins

Write `fewest_coins(amount, coins)` that returns the fewest coins from the
given denominations that add up exactly to `amount`, using each
denomination as many times as needed. Return `-1` if it cannot be made.
`amount` is zero or more.

```static
fewest_coins(30, [25, 10, 1])   ->  3      (10 + 10 + 10)
fewest_coins(67, [25, 10, 5, 1])  ->  6
fewest_coins(3, [2])            ->  -1
fewest_coins(0, [7])            ->  0
```

The point is to practise a one-dimensional DP table where greedy fails.

## Starter

```python
def fewest_coins(amount, coins):
    ...
```

## Hints

1. `table[a]` is the fewest coins for amount `a`. `table[0] = 0`; everything else starts as infinity (`float("inf")`).
2. For each amount from 1 up, for each coin that fits, `table[a] = min(table[a], table[a - coin] + 1)`.
3. If `table[amount]` is still infinity, return `-1`.

## Approach

Every amount's answer is one more than the best answer for the amount minus some coin. Fill amounts in increasing order so the smaller answers are ready. Cost `amount × len(coins)`.

## Reference

```python
def fewest_coins(amount, coins):
    INF = float("inf")
    table = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and table[a - c] + 1 < table[a]:
                table[a] = table[a - c] + 1
    return -1 if table[amount] == INF else table[amount]
```
