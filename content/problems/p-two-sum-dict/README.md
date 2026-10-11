# Two sum in one pass

Given a list of prices and a target, find two different positions whose
prices add up to the target. Checking every pair works but is slow for long
lists. A faster way: walk the list once, and for each price ask "have I
already seen the price that would complete this pair?" A dictionary from
price to position answers that instantly. If the answer is no, record the
current price and move on.

Write `two_sum(prices, target)` that returns the two positions as a tuple
`(earlier, later)`, or `None` if no pair works. Exactly one pair works when
one exists.

```static
two_sum([2, 7, 11, 15], 9)  ->  (0, 1)
two_sum([1, 2], 10)         ->  None
```

## Starter

```python
def two_sum(prices, target):
    ...
```

## Hints

1. `seen = {}` mapping price to index; for each price check `target - price in seen` before storing.
2. Checking before storing means a price is never paired with itself.

## Approach

One pass with a dictionary of what has been seen. The order of check-then-store is what makes `[3, 3]` with target 6 work and `[3]` not.

## Reference

```python
def two_sum(prices, target):
    seen = {}
    for i, price in enumerate(prices):
        if target - price in seen:
            return (seen[target - price], i)
        seen[price] = i
    return None
```
