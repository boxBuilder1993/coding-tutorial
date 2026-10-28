# Alphabet from a sorted word list

`words` is a list of words sorted according to an unknown alphabet. Write
`alien_order(words)` that returns a string of all the letters that appear, in an order
consistent with the list, or `""` if the list is contradictory (including a word
appearing after its own longer form, like `["abc", "ab"]`). Any consistent order passes.

```static
alien_order(["wrt", "wrf", "er", "ett", "rftt"])  ->  "wertf"
alien_order(["z", "x"])                           ->  "zx"
alien_order(["z", "x", "z"])                      ->  ""
```

Each pair of adjacent words gives one constraint from their first differing letter. Then
it is a topological sort; a cycle, or a prefix violation, means no answer.

## Starter

```python
def alien_order(words):
    ...
```

## Hints

1. Collect every letter. For adjacent words, find the first position where they differ: that gives `before -> after`. If they do not differ but the first is longer, return `""`.
2. Kahn's algorithm over the letters with the constraints as edges. If the output has fewer letters than exist, there was a cycle: return `""`.

## Approach

Constraints from adjacent pairs form a directed graph on letters; a topological order of it is the alphabet. Linear in total word length.

## Reference

```python
from collections import deque

def alien_order(words):
    letters = {ch for w in words for ch in w}
    after = {ch: set() for ch in letters}
    indeg = {ch: 0 for ch in letters}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in after[x]:
                    after[x].add(y)
                    indeg[y] += 1
                break
        else:
            if len(a) > len(b):
                return ""
    queue = deque(sorted(ch for ch in letters if indeg[ch] == 0))
    out = []
    while queue:
        ch = queue.popleft()
        out.append(ch)
        for nxt in after[ch]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                queue.append(nxt)
    return "".join(out) if len(out) == len(letters) else ""
```
