# First non-repeating character in a stream

Characters arrive one at a time. After each arrival, report the first
character seen so far that has appeared exactly once, or `"#"` if there is
none. Keep a count of each character in a dictionary, and a queue of
characters in arrival order. After each arrival, drop characters from the
front of the queue while their count is more than one; the front, if any,
is the answer.

Write `first_unique_stream(text)` that returns a string with one answer
character per arrival.

```static
first_unique_stream("aabc")  ->  "a#bb"
first_unique_stream("abab")  ->  "aab#"
```

## Starter

```python
from collections import deque

def first_unique_stream(text):
    ...
```

## Hints

1. Two structures: `counts` dict and a `deque` of characters.
2. After updating the count and appending: `while q and counts[q[0]] > 1: q.popleft()`. Answer is `q[0]` or `#`.

## Approach

Characters leave the queue only from the front and only once they have repeated, so each is enqueued and dequeued at most once. The queue front is always the earliest still-unique character.

## Reference

```python
from collections import deque

def first_unique_stream(text):
    counts = {}
    q = deque()
    out = []
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
        q.append(ch)
        while q and counts[q[0]] > 1:
            q.popleft()
        out.append(q[0] if q else "#")
    return "".join(out)
```
