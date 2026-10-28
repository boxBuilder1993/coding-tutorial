# All balanced bracket strings

Write `balanced(n)` that returns every string made of `n` `(` and `n` `)` that is
correctly balanced. Order of the output does not matter.

```static
balanced(1)  ->  ["()"]
balanced(2)  ->  ["(())", "()()"]
balanced(3)  ->  ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

The point is to practise pruning with two counters: add `(` while some remain, add `)`
only while there are more `(` than `)` so far.

## Starter

```python
def balanced(n):
    ...
```

## Hints

1. `go(open_count, close_count)`: when both reach `n`, record.
2. Add `(` if `open_count < n`; add `)` if `close_count < open_count`. Pop after each recursive call.

## Approach

The two rules make every partial string a valid prefix, so nothing is generated and then thrown away. The number of results is the Catalan number.

## Reference

```python
def balanced(n):
    out = []
    partial = []

    def go(open_count, close_count):
        if open_count == n and close_count == n:
            out.append("".join(partial))
            return
        if open_count < n:
            partial.append("(")
            go(open_count + 1, close_count)
            partial.pop()
        if close_count < open_count:
            partial.append(")")
            go(open_count, close_count + 1)
            partial.pop()

    go(0, 0)
    return out
```
