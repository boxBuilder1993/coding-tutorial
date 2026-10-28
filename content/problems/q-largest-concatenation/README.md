# Largest number from pieces

`nums` is a list of non-negative whole numbers. Write `largest_number(nums)` that
arranges them, as strings joined together, to make the largest possible number, and
returns it as a string.

```static
largest_number([10, 2])          ->  "210"
largest_number([3, 30, 34, 5, 9]) ->  "9534330"
largest_number([0, 0])           ->  "0"
```

The point is to practise sorting with a custom notion of order. Comparing `a + b`
against `b + a` decides which of two pieces should come first.

## Starter

```python
def largest_number(nums):
    ...
```

## Hints

1. Convert to strings. `a` should come before `b` when `a + b > b + a`.
2. `functools.cmp_to_key` turns a two-argument comparison into a `key` for `sorted`. Return `-1`, `0` or `1` from the comparison.
3. Strip leading zeros at the end, keeping at least one digit.

## Approach

Sort the strings with a comparison that puts `a` first when `a + b` is the bigger string. `cmp_to_key` adapts the comparison for `sorted`. Join, then collapse an all-zero answer to a single zero.

## Reference

```python
from functools import cmp_to_key

def largest_number(nums):
    strs = [str(n) for n in nums]
    def compare(a, b):
        if a + b > b + a:
            return -1
        if a + b < b + a:
            return 1
        return 0
    strs.sort(key=cmp_to_key(compare))
    result = "".join(strs).lstrip("0")
    return result or "0"
```
