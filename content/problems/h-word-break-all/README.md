# Every way to split into words

Write `all_breaks(text, words)` that returns every way to split `text` into a sequence of
words from `words` (reusable), each as a space-separated sentence. Order of the output
does not matter.

```static
all_breaks("catsanddog", ["cat", "cats", "and", "sand", "dog"])  ->  ["cats and dog", "cat sand dog"]
all_breaks("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
    ->  ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
all_breaks("catsandog", ["cats", "dog", "sand", "and", "cat"])  ->  []
```

Backtracking over prefixes, with memoisation of "all sentences for the suffix starting at
`i`" so that shared suffixes are not re-explored.

## Starter

```python
def all_breaks(text, words):
    ...
```

## Hints

1. `memo = {}`; `go(i)` returns the list of sentences for `text[i:]`; `go(len(text))` is `[""]`.
2. For each `end` with `text[i:end]` in the word set, for each `rest` in `go(end)`, produce the word plus (a space plus `rest` if `rest` is non-empty).
3. Store in `memo[i]` before returning.

## Approach

Top-down DP whose values are lists of sentences. Memoisation keeps the search from re-solving suffixes; the output itself can be exponential, so inputs stay small.

## Reference

```python
def all_breaks(text, words):
    pool = set(words)
    memo = {}

    def go(i):
        if i == len(text):
            return [""]
        if i in memo:
            return memo[i]
        out = []
        for end in range(i + 1, len(text) + 1):
            piece = text[i:end]
            if piece in pool:
                for rest in go(end):
                    out.append(piece if rest == "" else piece + " " + rest)
        memo[i] = out
        return out

    return go(0)
```
