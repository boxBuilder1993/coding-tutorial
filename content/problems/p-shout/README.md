# Shout it

Write `shout(text)` that returns the text in capitals with an exclamation mark
added at the end.

```static
shout("fresh bread")  ->  "FRESH BREAD!"
```

## Starter

```python
def shout(text):
    ...
```

## Hints

1. A string method, then `+`.
2. `text.upper() + "!"`

## Approach

`upper` returns a new string; join the `!` on with `+` or an f-string.

## Reference

```python
def shout(text):
    return text.upper() + "!"
```
