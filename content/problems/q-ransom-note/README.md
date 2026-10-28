# Can the note be made?

Write `can_make(note, magazine)` that returns `True` if every character of `note` can
be cut from `magazine`, each magazine character used at most once. Spaces count as
characters.

```static
can_make("aa", "aab")   ->  True
can_make("aa", "ab")    ->  False
can_make("", "x")       ->  True
```

The point is to practise Counter subtraction as a containment test.

## Starter

```python
def can_make(note, magazine):
    ...
```

## Hints

1. `Counter(note) - Counter(magazine)` is empty exactly when the magazine has enough of everything.
2. An empty Counter is falsy, so `not (Counter(note) - Counter(magazine))` is the answer.

## Approach

Subtracting counters drops non-positive counts, so what remains is what the magazine lacks. Empty remainder means possible.

## Reference

```python
from collections import Counter

def can_make(note, magazine):
    return not (Counter(note) - Counter(magazine))
```
