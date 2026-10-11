# Word counts

Write `word_counts(text)` that returns a dictionary of how many times each
word appears, treating capitals and lowercase as the same word.

```static
word_counts("Bread and milk and bread")  ->  {"bread": 2, "and": 2, "milk": 1}
```

## Starter

```python
def word_counts(text):
    ...
```

## Hints

1. `lower` and `split`, then the counting pattern.
2. `for word in text.lower().split():` then `get(word, 0) + 1`.

## Approach

Normalise case before splitting so the two breads count together.

## Reference

```python
def word_counts(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```
