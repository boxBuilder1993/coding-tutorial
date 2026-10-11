# Capitalise each word

Write `title_case(text)` that capitalises the first letter of every word
and lowercases the rest. Words are separated by single spaces.

```static
title_case("fresh SOURDOUGH bread")  ->  "Fresh Sourdough Bread"
```

## Starter

```python
def title_case(text):
    ...
```

## Hints

1. `split`, fix each word with slicing and methods, `join`.
2. `word[0].upper() + word[1:].lower()`

## Approach

Rebuild each word from its first character and the rest, then join with spaces.

## Reference

```python
def title_case(text):
    words = []
    for word in text.split():
        words.append(word[0].upper() + word[1:].lower())
    return " ".join(words)
```
