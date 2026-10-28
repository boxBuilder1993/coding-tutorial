# Longest palindromic stretch

Write `longest_palindrome(text)` that returns the longest stretch of consecutive
characters that reads the same backwards. If several tie, return the leftmost.

```static
longest_palindrome("babad")  ->  "bab"
longest_palindrome("cbbd")   ->  "bb"
longest_palindrome("")       ->  ""
```

Expand around every centre, both a single character and the gap between two characters.
Quadratic in the worst case, which is fine for a few thousand characters.

## Starter

```python
def longest_palindrome(text):
    ...
```

## Hints

1. For each `i`, try centres `(i, i)` and `(i, i + 1)`: widen `l` and `r` while in bounds and `text[l] == text[r]`.
2. Keep the longest; use `>` rather than `>=` so the leftmost wins ties.

## Approach

Every palindrome has a centre; expanding from each of the `2n - 1` centres finds the longest in quadratic time with no table.

## Reference

```python
def longest_palindrome(text):
    best = ""
    for i in range(len(text)):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < len(text) and text[l] == text[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(best):
                best = text[l + 1:r]
    return best
```
