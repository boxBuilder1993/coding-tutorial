# Longest stretch without repeats

Find the length of the longest stretch of a string with no repeated
characters. Keep a window `[left, right]` and a set of the characters in
it. Move `right` one step at a time; if the new character is already in
the set, move `left` rightwards, removing characters from the set, until
it is not. The window is then valid again; record its length.

Write `longest_unique(text)`.

```static
longest_unique("abcabcbb")  ->  3
longest_unique("bbbbb")     ->  1
longest_unique("")          ->  0
```

## Starter

```python
def longest_unique(text):
    ...
```

## Hints

1. `seen = set()`, `left = 0`, `best = 0`; `for right, ch in enumerate(text):`.
2. `while ch in seen: seen.remove(text[left]); left += 1`, then `seen.add(ch)` and `best = max(best, right - left + 1)`.

## Approach

The window only ever grows on the right and shrinks on the left, so each character enters and leaves the set at most once.

## Reference

```python
def longest_unique(text):
    seen = set()
    left = 0
    best = 0
    for right, ch in enumerate(text):
        while ch in seen:
            seen.remove(text[left])
            left += 1
        seen.add(ch)
        best = max(best, right - left + 1)
    return best
```
