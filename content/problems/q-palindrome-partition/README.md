# Cut into palindromes

Write `palindrome_cuts(text)` that returns every way to cut `text` into pieces that are
each a palindrome, as a list of lists of strings. Order of the output does not matter.

```static
palindrome_cuts("aab")  ->  [["a", "a", "b"], ["aa", "b"]]
palindrome_cuts("a")    ->  [["a"]]
```

The point is to practise backtracking over cut positions, pruning any prefix that is not
a palindrome.

## Starter

```python
def palindrome_cuts(text):
    ...
```

## Hints

1. `go(start)`: if `start == len(text)`, record. For each `end` from `start + 1` to `len`, if `text[start:end]` is a palindrome, append it, recurse with `end`, pop.
2. `s == s[::-1]` tests a palindrome.

## Approach

Choose the next piece from the current position, only among palindromic prefixes. Every valid partition is reached once.

## Reference

```python
def palindrome_cuts(text):
    out = []
    partial = []

    def go(start):
        if start == len(text):
            out.append(partial[:])
            return
        for end in range(start + 1, len(text) + 1):
            piece = text[start:end]
            if piece == piece[::-1]:
                partial.append(piece)
                go(end)
                partial.pop()

    go(0)
    return out
```
