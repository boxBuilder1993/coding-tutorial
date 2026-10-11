# Initials

Write `initials(name)` that returns the first letter of each word, in
capitals, joined together. The name has at least one word.

```static
initials("ada lovelace")      ->  "AL"
initials("grace brewster hopper")  ->  "GBH"
```

## Starter

```python
def initials(name):
    ...
```

## Hints

1. `split`, then the first character of each word.
2. Build a string: `result += word[0].upper()`.

## Approach

Split into words, take `[0]` of each, uppercase, accumulate.

## Reference

```python
def initials(name):
    result = ""
    for word in name.split():
        result += word[0].upper()
    return result
```
