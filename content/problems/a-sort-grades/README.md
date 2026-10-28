# Sort grades without comparing

`grades` is a list of letters from `"A"` to `"F"` (no `"E"`). Write
`sort_grades(grades)` that returns them sorted from `"A"` to `"F"`
using counting: tally how many of each grade there are, then build the
result from the tallies in order.

```static
sort_grades(["C", "A", "F", "B", "A", "C"])  ->  ["A", "A", "B", "C", "C", "F"]
sort_grades([])                              ->  []
```

The point is to practise counting sort, so do it with counts rather than
`sorted`.

## Starter

```python
def sort_grades(grades):
    ...
```

## Hints

1. The order is fixed: `"ABCDF"`. Count each grade with a dictionary or a `Counter`.
2. Loop over `"ABCDF"` and extend the result with `[grade] * count`.

## Approach

One linear pass to count, one pass over the five possible grades to write them out. The result is sorted without any comparison between items.

## Reference

```python
def sort_grades(grades):
    counts = {g: 0 for g in "ABCDF"}
    for g in grades:
        counts[g] += 1
    out = []
    for g in "ABCDF":
        out.extend([g] * counts[g])
    return out
```
