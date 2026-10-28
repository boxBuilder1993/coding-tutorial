# Change with standard coins

Coins come in `[25, 10, 5, 1]`. Write `change(amount)` that returns the
list of coins, largest first, that makes `amount` with the fewest coins.
`amount` is zero or more.

```static
change(67)  ->  [25, 25, 10, 5, 1, 1]
change(30)  ->  [25, 5]
change(0)   ->  []
```

The point is to practise a greedy loop, and to notice that it is correct
for these coins because every coin is a multiple of the one below it,
except the 25, which the 10 and 5 fill under neatly. Change the coins to
`[25, 10, 1]` and the same code gives six coins for 30 where three would
do.

## Starter

```python
def change(amount):
    ...
```

## Hints

1. For each coin from largest to smallest, `while amount >= coin`: subtract it and append it.
2. The result list is already largest-first because of the loop order.

## Approach

Take the largest coin that fits until it no longer does, then move to the next coin. Linear in the number of coins returned.

## Reference

```python
def change(amount):
    used = []
    for coin in [25, 10, 5, 1]:
        while amount >= coin:
            amount -= coin
            used.append(coin)
    return used
```
