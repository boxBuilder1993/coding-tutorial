# Count the vowels

Write `vowels(text)` that returns how many characters of `text` are vowels:
`a`, `e`, `i`, `o` or `u`, lowercase only.

```static
vowels("sourdough")  ->  4
vowels("xyz")        ->  0
```

## Starter

```python
def vowels(text):
    ...
```

## Hints

1. A loop over the characters with `in`.
2. `if ch in "aeiou":` then add one to a count.

## Approach

Accumulate a count, testing each character against the string of vowels.

## Reference

```python
def vowels(text):
    count = 0
    for ch in text:
        if ch in "aeiou":
            count += 1
    return count
```
