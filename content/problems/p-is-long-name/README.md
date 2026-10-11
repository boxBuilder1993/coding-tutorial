# Long name?

Write `is_long(name)` that returns `True` if the name has more than ten
characters.

```static
is_long("sourdough bread")  ->  True
is_long("milk")             ->  False
```

## Starter

```python
def is_long(name):
    ...
```

## Hints

1. `len` and `>`.
2. `return len(name) > 10`

## Approach

Compare the length; the comparison is already a boolean.

## Reference

```python
def is_long(name):
    return len(name) > 10
```
