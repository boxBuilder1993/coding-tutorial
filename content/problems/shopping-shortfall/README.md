# Shopping shortfall

Write `shortfall(needed, have)` that takes two lists of item names, one
listing what a recipe needs (with repeats for quantities) and one listing
what is in the kitchen, and returns a dictionary of what to buy: each
missing item with how many more are needed. Items that are fully covered
do not appear.

```static
shortfall(["egg", "egg", "egg", "milk"], ["egg", "butter"])  ->  {"egg": 2, "milk": 1}
shortfall(["egg"], ["egg", "egg"])                           ->  {}
```

The point is to practise Counter subtraction.

## Starter

```python
def shortfall(needed, have):
    ...
```

## Hints

1. Build a Counter from each list.
2. `Counter(needed) - Counter(have)` keeps only the positive differences.
3. Wrap the result in `dict(...)` so it compares equal to a plain dictionary.

## Approach

`dict(Counter(needed) - Counter(have))`. Subtraction drops zero and negative counts, which is exactly the "fully covered items do not appear" rule.

## Reference

```python
from collections import Counter

def shortfall(needed, have):
    return dict(Counter(needed) - Counter(have))
```
