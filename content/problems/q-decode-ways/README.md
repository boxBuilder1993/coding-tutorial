# Ways to decode digits

Letters were encoded as numbers, `A = 1` through `Z = 26`, and the digits concatenated.
Write `decode_ways(digits)` that returns how many ways the digit string can be decoded.
A `0` can only be part of `10` or `20`.

```static
decode_ways("12")   ->  2     (AB or L)
decode_ways("226")  ->  3     (BZ, VF, BBF)
decode_ways("06")   ->  0
```

The point is to practise a DP over string prefixes with two possible last steps.

## Starter

```python
def decode_ways(digits):
    ...
```

## Hints

1. `ways[i]` = decodings of the first `i` digits; `ways[0] = 1`.
2. If `digits[i - 1] != "0"`, add `ways[i - 1]`. If `i >= 2` and `10 <= int(digits[i - 2:i]) <= 26`, add `ways[i - 2]`.

## Approach

The last letter used one or two digits; count both if they are valid. Linear.

## Reference

```python
def decode_ways(digits):
    n = len(digits)
    ways = [1] + [0] * n
    for i in range(1, n + 1):
        if digits[i - 1] != "0":
            ways[i] += ways[i - 1]
        if i >= 2 and 10 <= int(digits[i - 2:i]) <= 26:
            ways[i] += ways[i - 2]
    return ways[n]
```
