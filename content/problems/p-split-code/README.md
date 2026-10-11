# Split a product code

Product codes look like `BRD-001-A`: department, number and batch separated
by dashes. Write `parts(code)` that returns the three pieces as a tuple.

```static
parts("BRD-001-A")  ->  ("BRD", "001", "A")
```

## Starter

```python
def parts(code):
    ...
```

## Hints

1. `split` takes a separator argument.
2. `tuple(code.split("-"))`

## Approach

`split("-")` gives a list of three; `tuple` converts it.

## Reference

```python
def parts(code):
    return tuple(code.split("-"))
```
