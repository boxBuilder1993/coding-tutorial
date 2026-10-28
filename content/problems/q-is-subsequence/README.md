# Is it a subsequence?

Write `is_subsequence(small, big)` that returns `True` if the characters of `small`
appear in `big` in the same order, not necessarily next to each other.

```static
is_subsequence("ace", "abcde")  ->  True
is_subsequence("aec", "abcde")  ->  False
is_subsequence("", "abc")       ->  True
```

The point is to practise two pointers over two different sequences.

## Starter

```python
def is_subsequence(small, big):
    ...
```

## Hints

1. One index into `small`. Walk `big`; whenever the current `big` character matches `small[i]`, advance `i`.
2. The answer is whether `i` reached `len(small)`.

## Approach

Greedy matching: take the earliest possible match for each character of `small`. One pass over `big`.

## Reference

```python
def is_subsequence(small, big):
    i = 0
    for ch in big:
        if i < len(small) and ch == small[i]:
            i += 1
    return i == len(small)
```
