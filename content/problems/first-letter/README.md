# First letter

Write `first_letter(name)` that returns the first character of `name`, in
capitals. You can capitalise with `.upper()`.

```static
first_letter("bread")  ->  "B"
first_letter("Milk")   ->  "M"
```

`name` always has at least one character.

## Starter

```python
def first_letter(name):
    ...
```

## Hints

1. The first character is at position 0: `name[0]`.
2. Call `.upper()` on it: `name[0].upper()`.

## Approach

Index position 0, then uppercase the result.

## Reference

```python
def first_letter(name):
    return name[0].upper()
```
