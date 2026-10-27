# Group by length

Write `group_by_length(words)` that returns a dictionary from word length
to the list of words with that length, in the order they appeared.

```static
group_by_length(["apple", "milk", "bread", "eggs"])  ->  {5: ["apple", "bread"], 4: ["milk", "eggs"]}
group_by_length([])  ->  {}
```

The point is to practise grouping with `defaultdict(list)`.

## Starter

```python
def group_by_length(words):
    ...
```

## Hints

1. `groups = defaultdict(list)`, then for each word `groups[len(word)].append(word)`.
2. Return `dict(groups)` so the checks see a plain dictionary.

## Approach

A `defaultdict(list)` makes the empty list for each new length automatically. Loop once, appending each word under its length, and convert to `dict` at the end.

## Reference

```python
from collections import defaultdict

def group_by_length(words):
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)
```
