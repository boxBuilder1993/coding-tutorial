# Longest stretch with at most k distinct letters

Write `longest_k_distinct(text, k)` that returns the length of the longest run of
consecutive characters containing at most `k` different characters. `k` is at least 1.

```static
longest_k_distinct("eceba", 2)  ->  3     ("ece")
longest_k_distinct("aa", 1)     ->  2
longest_k_distinct("abcabc", 3) ->  6
```

The point is to practise a variable window whose state is a `Counter` of what is inside.

## Starter

```python
def longest_k_distinct(text, k):
    ...
```

## Hints

1. Keep a `Counter` of characters in the window. Add the right character; while the counter has more than `k` keys, remove the left character (and delete the key when its count hits zero).
2. Record the window length when it is valid.

## Approach

Distinct count is `len(counter)` as long as zero-count keys are deleted. Grow right, shrink left when over `k`. Linear.

## Reference

```python
from collections import Counter

def longest_k_distinct(text, k):
    counts = Counter()
    left = 0
    best = 0
    for right, ch in enumerate(text):
        counts[ch] += 1
        while len(counts) > k:
            counts[text[left]] -= 1
            if counts[text[left]] == 0:
                del counts[text[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
```
