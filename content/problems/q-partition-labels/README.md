# Cut into self-contained pieces

Write `partition_sizes(text)` that cuts `text` into as many pieces as possible such that
each letter appears in only one piece, and returns the piece lengths in order.

```static
partition_sizes("ababcbacadefegdehijhklij")  ->  [9, 7, 8]
partition_sizes("abc")                       ->  [1, 1, 1]
partition_sizes("aaa")                       ->  [3]
```

The point is to practise a greedy that extends the current piece to the last occurrence
of every letter it contains.

## Starter

```python
def partition_sizes(text):
    ...
```

## Hints

1. First pass: `last[ch]` = last index of each letter.
2. Second pass: track `end = max(end, last[ch])`; when `i == end`, a piece closes: record its length and start the next.

## Approach

A piece cannot end before the last occurrence of any letter inside it, and ending exactly there is the greedy that maximises piece count. Two linear passes.

## Reference

```python
def partition_sizes(text):
    last = {ch: i for i, ch in enumerate(text)}
    out = []
    start = end = 0
    for i, ch in enumerate(text):
        end = max(end, last[ch])
        if i == end:
            out.append(end - start + 1)
            start = i + 1
    return out
```
