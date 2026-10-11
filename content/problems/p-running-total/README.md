# Running total

Write `running(amounts)` that returns a list where each position holds the
sum of all amounts up to and including that one.

```static
running([10, 5, 20])  ->  [10, 15, 35]
running([])           ->  []
```

## Starter

```python
def running(amounts):
    ...
```

## Hints

1. Accumulate a total and append it after every step.
2. `total += x` then `result.append(total)`.

## Approach

One accumulator, appended each time it changes.

## Reference

```python
def running(amounts):
    result = []
    total = 0
    for x in amounts:
        total += x
        result.append(total)
    return result
```
