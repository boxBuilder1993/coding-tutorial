# Last three characters

Product codes end in a three-character batch number. Write `batch(code)` that
returns the last three characters of `code`.

```static
batch("SKU-1042-A7B")  ->  "A7B"
batch("BRD-001")       ->  "001"
```

`code` always has at least three characters.

## Starter

```python
def batch(code):
    ...
```

## Hints

1. A slice with a negative start counts from the end.
2. `code[-3:]` is "from three before the end, to the end".

## Approach

Slice from `-3` to the end. `code[len(code) - 3:]` works too but is longer.

## Reference

```python
def batch(code):
    return code[-3:]
```
