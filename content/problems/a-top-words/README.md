# Top words

Write `top_words(text, k)` that returns the `k` most frequent words in
`text` (split on spaces), most frequent first. When two words have the
same count, the alphabetically earlier word comes first. `k` is at most the
number of distinct words.

```static
top_words("the cat sat on the mat the cat ran", 2)  ->  ["the", "cat"]
top_words("b a b a c", 3)                            ->  ["a", "b", "c"]
```

The point is to practise a `Counter` feeding a heap of tuples, where the
tuple order handles the tie-break for you.

## Starter

```python
def top_words(text, k):
    ...
```

## Hints

1. `counts = Counter(text.split())`.
2. Make tuples `(-count, word)`: negative count so the most frequent is smallest, and the word as tie-break ascending.
3. `heapq.nsmallest(k, tuples)` then take the words.

## Approach

Count, then order by `(-count, word)`. With `nsmallest` the heap does the work; a full sort with the same key also passes. The negative count flips the min-heap into a max-heap while leaving the word tie-break ascending.

## Reference

```python
import heapq
from collections import Counter

def top_words(text, k):
    counts = Counter(text.split())
    return [w for c, w in heapq.nsmallest(k, ((-c, w) for w, c in counts.items()))]
```
