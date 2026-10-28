# Ways to make change

Write `change_ways(amount, coins)` that returns how many different combinations of the
given coin denominations add up to `amount`. Order does not matter: `1+2` and `2+1` are
the same combination. `change_ways(0, coins)` is 1.

```static
change_ways(5, [1, 2, 5])  ->  4     (5, 2+2+1, 2+1+1+1, 1+1+1+1+1)
change_ways(3, [2])        ->  0
change_ways(10, [10])      ->  1
```

The point is to practise the loop order that counts combinations rather than sequences:
coins outside, amounts inside.

## Starter

```python
def change_ways(amount, coins):
    ...
```

## Hints

1. `ways = [1] + [0] * amount`.
2. For each coin, for `a` from `coin` to `amount`: `ways[a] += ways[a - coin]`. Processing one coin fully before the next means each combination is counted once, in coin order.

## Approach

Adding coins one denomination at a time ensures combinations are built in a fixed order and never double-counted. `amount * len(coins)` steps.

## Reference

```python
def change_ways(amount, coins):
    ways = [1] + [0] * amount
    for coin in coins:
        for a in range(coin, amount + 1):
            ways[a] += ways[a - coin]
    return ways[amount]
```
