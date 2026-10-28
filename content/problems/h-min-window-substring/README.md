# Smallest window containing every letter

Write `min_window(text, letters)` that returns the shortest stretch of `text` that
contains every character of `letters`, including repeats, or `""` if none does. If several
stretches tie for shortest, return the leftmost.

```static
min_window("ADOBECODEBANC", "ABC")  ->  "BANC"
min_window("a", "aa")               ->  ""
```

A variable window with a `Counter` of what is still needed and a count of how many
requirements are unmet. Grow from the right until everything is covered, shrink from the
left while it stays covered. One check is a hundred thousand characters.

## Starter

```python
def min_window(text, letters):
    ...
```

## Hints

1. `need = Counter(letters)`; `missing = len(letters)`. Adding a character whose need is still positive decrements `missing`; always decrement its need.
2. When `missing == 0`, shrink from the left: increment the left character's need; if it becomes positive, `missing += 1` and stop shrinking. Record the window before each shrink step.
3. Characters not in `letters` go negative in the counter, which is harmless: they never affect `missing`. Guard the empty-`letters` case, or the shrinking loop never stops.

## Approach

Classic two-pointer window. Each character enters and leaves once. Linear.

## Reference

```python
from collections import Counter

def min_window(text, letters):
    if not letters:
        return ""
    need = Counter(letters)
    missing = len(letters)
    left = 0
    best = (0, 0)
    best_len = float("inf")
    for right, ch in enumerate(text):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best = (left, right + 1)
            need[text[left]] += 1
            if need[text[left]] > 0:
                missing += 1
            left += 1
    return text[best[0]:best[1]] if best_len != float("inf") else ""
```
