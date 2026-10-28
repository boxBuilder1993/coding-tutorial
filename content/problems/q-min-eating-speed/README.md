# Slowest speed that finishes in time

`piles` lists how many bananas are in each pile, and you have `hours` to eat them all.
Each hour you pick one pile and eat up to `k` bananas from it; if the pile has fewer than
`k` left you finish it and the rest of that hour is wasted. Write `min_speed(piles, hours)`
that returns the smallest `k` that lets you finish within `hours`. `hours` is at least
`len(piles)`.

```static
min_speed([3, 6, 7, 11], 8)   ->  4
min_speed([30, 11, 23, 4, 20], 5)  ->  30
min_speed([30, 11, 23, 4, 20], 6)  ->  23
```

The point is to practise binary search on an answer with a helper that checks a guess.

## Starter

```python
def min_speed(piles, hours):
    ...
```

## Hints

1. Hours needed at speed `k` is the sum over piles of `ceil(pile / k)`, which is `(pile + k - 1) // k` in whole numbers.
2. Search `k` from 1 to `max(piles)`: if the hours needed fit, record and try slower; otherwise go faster.

## Approach

A speed either works or does not, and faster always works if slower does. Binary search the speed; each check is a linear pass over the piles.

## Reference

```python
def min_speed(piles, hours):
    def hours_at(k):
        return sum((p + k - 1) // k for p in piles)

    low, high = 1, max(piles)
    best = high
    while low <= high:
        mid = (low + high) // 2
        if hours_at(mid) <= hours:
            best = mid
            high = mid - 1
        else:
            low = mid + 1
    return best
```
