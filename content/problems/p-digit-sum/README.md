# Sum of digits

Write `digit_sum(n)` that returns the sum of the digits of a non-negative
whole number.

```static
digit_sum(1234)  ->  10
digit_sum(0)     ->  0
```

## Starter

```python
def digit_sum(n):
    ...
```

## Hints

1. Turn the number into text to loop over its characters, then `int` each one.
2. `for ch in str(n): total += int(ch)`

## Approach

`str` gives the digits as characters; `int` turns each back into a number.

## Reference

```python
def digit_sum(n):
    total = 0
    for ch in str(n):
        total += int(ch)
    return total
```
