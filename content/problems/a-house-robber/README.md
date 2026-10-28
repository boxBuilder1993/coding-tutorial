# House robber

`houses` lists the cash in each house along a street. You may not take
from two adjacent houses. Write `most_cash(houses)` that returns the most
you can take.

```static
most_cash([2, 7, 9, 3, 1])  ->  12     (2 + 9 + 1)
most_cash([1, 2, 3, 1])     ->  4      (1 + 3)
most_cash([])               ->  0
```

The point is to practise the take-or-skip recurrence.

## Starter

```python
def most_cash(houses):
    ...
```

## Hints

1. Let `best(i)` be the most from the first `i` houses. For house `i`: skip it (`best(i - 1)`) or take it (`best(i - 2) + houses[i]`). Take the larger.
2. Two variables for the previous two answers are enough: `prev2, prev1 = prev1, max(prev1, prev2 + cash)`.

## Approach

Walk the street once. At each house the best so far is the larger of "same as before this house" and "two houses back plus this one". Linear, constant space.

## Reference

```python
def most_cash(houses):
    prev2, prev1 = 0, 0
    for cash in houses:
        prev2, prev1 = prev1, max(prev1, prev2 + cash)
    return prev1
```
