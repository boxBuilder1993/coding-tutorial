# Can the text be split into words?

Write `can_break(text, words)` that returns whether `text` can be split into a sequence of
words from the list `words`, with words reusable.

```static
can_break("leetcode", ["leet", "code"])              ->  True
can_break("applepenapple", ["apple", "pen"])         ->  True
can_break("catsandog", ["cats", "dog", "sand", "and", "cat"])  ->  False
```

The point is to practise a DP over prefixes: a prefix is breakable if it ends with a word
whose preceding prefix is breakable.

## Starter

```python
def can_break(text, words):
    ...
```

## Hints

1. `ok[0] = True`. For each end `i`, for each word `w`: if `ok[i - len(w)]` and `text[i - len(w):i] == w`, then `ok[i] = True`.
2. Put the words in a set and try every start `j < i` with `ok[j] and text[j:i] in words` as an alternative.

## Approach

Each prefix asks whether some word finishes it on top of a breakable shorter prefix. Length times number of words.

## Reference

```python
def can_break(text, words):
    ok = [True] + [False] * len(text)
    for i in range(1, len(text) + 1):
        for w in words:
            if i >= len(w) and ok[i - len(w)] and text[i - len(w):i] == w:
                ok[i] = True
                break
    return ok[len(text)]
```
