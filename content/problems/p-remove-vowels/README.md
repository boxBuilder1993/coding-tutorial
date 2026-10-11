# Remove the vowels

Write `no_vowels(text)` that returns the text with every lowercase vowel
removed.

```static
no_vowels("sourdough bread")  ->  "srdgh brd"
```

## Starter

```python
def no_vowels(text):
    ...
```

## Hints

1. Loop over characters, keep the ones not in `"aeiou"`, join.
2. `if ch not in "aeiou": kept.append(ch)` then `"".join(kept)`.

## Approach

Filter characters into a list and join, or build a string with `+=`.

## Reference

```python
def no_vowels(text):
    kept = []
    for ch in text:
        if ch not in "aeiou":
            kept.append(ch)
    return "".join(kept)
```
