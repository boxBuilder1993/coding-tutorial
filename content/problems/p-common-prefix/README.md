# Common prefix

Write `common_prefix(a, b)` that returns the longest string that both `a`
and `b` start with.

```static
common_prefix("sourdough", "soup")  ->  "sou"
common_prefix("milk", "bread")      ->  ""
```

## Starter

```python
def common_prefix(a, b):
    ...
```

## Hints

1. Walk both strings together with `zip` and stop at the first difference.
2. `for x, y in zip(a, b): if x != y: break` and build the prefix as you go.

## Approach

`zip` pairs characters by position and stops at the shorter string; `break` on the first mismatch.

## Reference

```python
def common_prefix(a, b):
    prefix = ""
    for x, y in zip(a, b):
        if x != y:
            break
        prefix += x
    return prefix
```
