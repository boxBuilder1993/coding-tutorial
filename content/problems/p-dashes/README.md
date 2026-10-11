# A line of dashes

Write `rule(n)` that returns a string of `n` dashes, for underlining a
receipt. `rule(0)` is the empty string.

```static
rule(5)  ->  "-----"
```

## Starter

```python
def rule(n):
    ...
```

## Hints

1. String repetition with `*`.
2. `"-" * n`

## Approach

`*` on a string repeats it.

## Reference

```python
def rule(n):
    return "-" * n
```
