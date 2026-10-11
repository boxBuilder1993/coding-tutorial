# Palindrome, ignoring case and spaces

Write `is_palindrome(text)` that returns `True` if the text reads the same
backwards, ignoring capital letters and spaces.

```static
is_palindrome("Was it a cat I saw")  ->  True
is_palindrome("bread")               ->  False
```

## Starter

```python
def is_palindrome(text):
    ...
```

## Hints

1. Clean the text first, then compare with its reverse.
2. `cleaned = text.lower().replace(" ", "")` then `cleaned == cleaned[::-1]`.

## Approach

Normalise with `lower` and `replace`, then one slice comparison.

## Reference

```python
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
```
