# Every mix of upper and lower case

Write `case_variants(text)` that returns every string obtainable by changing the case of
any letters in `text`; digits stay as they are. Order of the output does not matter.

```static
case_variants("a1b")  ->  ["a1b", "a1B", "A1b", "A1B"]
case_variants("12")   ->  ["12"]
```

The point is to practise a two-way branch per position, with a position that offers only
one choice.

## Starter

```python
def case_variants(text):
    ...
```

## Hints

1. Recurse on the index. At a letter, branch on lower and upper; at a digit, one branch.
2. Build with a list of characters and join at the base case.

## Approach

Each letter doubles the count; digits do not. The template with a per-position choice list.

## Reference

```python
def case_variants(text):
    out = []
    chars = list(text)

    def go(i):
        if i == len(chars):
            out.append("".join(chars))
            return
        if chars[i].isalpha():
            chars[i] = chars[i].lower()
            go(i + 1)
            chars[i] = chars[i].upper()
            go(i + 1)
        else:
            go(i + 1)

    go(0)
    return out
```
