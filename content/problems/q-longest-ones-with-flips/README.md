# Longest run of ones with k flips

`bits` is a list of `0`s and `1`s. Write `longest_ones(bits, k)` that returns the longest
run of consecutive items you could make all `1` by flipping at most `k` zeros.

```static
longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)  ->  6
longest_ones([0, 0, 0], 0)                          ->  0
longest_ones([0, 0], 5)                             ->  2
```

The point is to practise a variable window whose validity rule is "at most k zeros inside".

## Starter

```python
def longest_ones(bits, k):
    ...
```

## Hints

1. Count zeros inside the window. Extend the right end; when zeros exceed `k`, move the left end right until they do not.
2. Record `right - left + 1` whenever the window is valid.

## Approach

Grow from the right, shrink from the left when the zero count passes `k`. Both ends move only forward, so linear.

## Reference

```python
def longest_ones(bits, k):
    left = 0
    zeros = 0
    best = 0
    for right, b in enumerate(bits):
        if b == 0:
            zeros += 1
        while zeros > k:
            if bits[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```
