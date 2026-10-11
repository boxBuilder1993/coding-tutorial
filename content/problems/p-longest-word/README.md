# Longest word

Write `longest_word(sentence)` that returns the longest word in a sentence
with at least one word. On a tie, return the first.

```static
longest_word("fresh sourdough bread")  ->  "sourdough"
```

## Starter

```python
def longest_word(sentence):
    ...
```

## Hints

1. `split`, then `max` with `key=len`, or a find-the-biggest loop.
2. `max(sentence.split(), key=len)` keeps the first on ties.

## Approach

`max` with `key=len` does the comparison by length and keeps the first of equals.

## Reference

```python
def longest_word(sentence):
    return max(sentence.split(), key=len)
```
