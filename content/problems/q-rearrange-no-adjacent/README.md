# No two neighbours alike

Write `rearrange(text)` that returns a rearrangement of the characters of `text` in which
no two adjacent characters are the same, or `""` if that is impossible. Any valid
arrangement passes.

```static
rearrange("aab")   ->  "aba"
rearrange("aaab")  ->  ""
rearrange("aabb")  ->  "abab"  or "baba"
```

The point is to practise a max-heap by count: always place the most frequent remaining
character, but never the one you just placed.

## Starter

```python
def rearrange(text):
    ...
```

## Hints

1. Heap of `(-count, char)`. Pop the most frequent; if it equals the last character placed, pop the next one instead and push the first back.
2. After placing, decrement the count and push back if positive. If you ever have nothing valid to place, return `""`.
3. Quick impossibility test: a character with more than `(len + 1) // 2` copies cannot be separated.

## Approach

Greedy with a heap: placing the most common remaining character first keeps the others available to separate it. Each step is log of the alphabet size.

## Reference

```python
import heapq
from collections import Counter

def rearrange(text):
    heap = [(-n, ch) for ch, n in Counter(text).items()]
    heapq.heapify(heap)
    out = []
    prev = None
    while heap:
        count, ch = heapq.heappop(heap)
        if out and out[-1] == ch:
            if not heap:
                return ""
            count2, ch2 = heapq.heappop(heap)
            out.append(ch2)
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, ch2))
            heapq.heappush(heap, (count, ch))
        else:
            out.append(ch)
            if count + 1 < 0:
                heapq.heappush(heap, (count + 1, ch))
    return "".join(out)
```
