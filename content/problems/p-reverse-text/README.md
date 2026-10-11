# Reverse the text

Write `backwards(text)` that returns the text reversed.

```static
backwards("bread")  ->  "daerb"
```

## Starter

```python
def backwards(text):
    ...
```

## Hints

1. A slice with step -1.
2. `text[::-1]`

## Approach

A step of -1 walks the string from the end.

## Reference

```python
def backwards(text):
    return text[::-1]
```
