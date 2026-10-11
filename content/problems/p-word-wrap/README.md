# Wrap a label

Write `wrap(text, width)` that breaks a sentence into lines no longer than
`width` characters, breaking only between words and fitting as many words
per line as possible. Every word is shorter than `width`.

```static
wrap("fresh sourdough bread baked daily", 12)  ->  ["fresh", "sourdough", "bread baked", "daily"]
```

## Starter

```python
def wrap(text, width):
    ...
```

## Hints

1. Keep a current line; if adding the next word (plus a space) would exceed the width, start a new line.
2. Track the current line as a list of words and compute its length with `len(" ".join(line))`.

## Approach

Greedy line filling. The length check must include the space that joining adds.

## Reference

```python
def wrap(text, width):
    lines = []
    current = []
    for word in text.split():
        candidate = " ".join(current + [word])
        if current and len(candidate) > width:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines
```
