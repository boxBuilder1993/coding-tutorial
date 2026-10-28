# Longest run summing to zero

Write `longest_zero_run(nums)` that returns the length of the longest run of
consecutive items whose sum is zero, or `0` if there is none.

```static
longest_zero_run([1, -1, 3, 2, -2, -3, 3])  ->  6     ([1, -1, 3, 2, -2, -3])
longest_zero_run([1, 2, 3])                  ->  0
longest_zero_run([0, 0, 0])                  ->  3
```

The point is to practise prefix sums with a dictionary of **first** occurrences: two
equal prefix sums bracket a zero-sum run.

## Starter

```python
def longest_zero_run(nums):
    ...
```

## Hints

1. Record the first index at which each prefix sum occurs, starting with `{0: -1}`.
2. When the current prefix was seen before at index `j`, the run from `j + 1` to here sums to zero; its length is `i - j`. Keep the longest.
3. Do not overwrite a first occurrence; earlier is longer.

## Approach

A zero-sum run is two equal prefix sums. Storing the earliest index of each prefix makes each later match as long as possible. Linear.

## Reference

```python
def longest_zero_run(nums):
    first = {0: -1}
    prefix = 0
    best = 0
    for i, x in enumerate(nums):
        prefix += x
        if prefix in first:
            best = max(best, i - first[prefix])
        else:
            first[prefix] = i
    return best
```
