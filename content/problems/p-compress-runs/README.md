# Compress repeated letters

Write `compress(text)` that replaces each run of the same character with
the character followed by the run length, leaving single characters alone.

```static
compress("aaabccdddd")  ->  "a3bc2d4"
compress("abc")         ->  "abc"
compress("")            ->  ""
```

## Starter

```python
def compress(text):
    ...
```

## Hints

1. Walk the string keeping the current character and its count; emit when the character changes.
2. Remember to emit the final run after the loop ends.

## Approach

Track `current` and `count`. On a change, append `current` plus the count if it is more than one. The last run needs emitting after the loop.

## Reference

```python
def compress(text):
    if not text:
        return ""
    parts = []
    current = text[0]
    count = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            parts.append(current + (str(count) if count > 1 else ""))
            current = ch
            count = 1
    parts.append(current + (str(count) if count > 1 else ""))
    return "".join(parts)
```
