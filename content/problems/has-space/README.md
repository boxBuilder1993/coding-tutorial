# Has a space?

Write `has_space(text)` that returns `True` if `text` contains at least one
space character, and `False` otherwise.

```static
has_space("sourdough bread")  ->  True
has_space("bread")            ->  False
```

## Starter

```python
def has_space(text):
    ...
```

## Hints

1. `in` checks whether one string appears inside another.
2. A single space is the string `" "`: `" " in text`.

## Approach

`return " " in text`. The `in` operator already gives a boolean.

## Reference

```python
def has_space(text):
    return " " in text
```
