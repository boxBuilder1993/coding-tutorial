# Receipt line with an f-string

Write `receipt_line(item, quantity, price)` that returns one line of a
receipt in exactly this format, where the last number is quantity times price:

```static
receipt_line("bread", 3, 40)   ->  "3 x bread = 120"
receipt_line("milk", 2, 2.5)   ->  "2 x milk = 5.0"
```

## Starter

```python
def receipt_line(item, quantity, price):
    ...
```

## Hints

1. Put `f` before the opening quote, then write names inside `{}`.
2. The total can be computed inside the braces: `{quantity * price}`.

## Approach

`return f"{quantity} x {item} = {quantity * price}"`. The f-string converts each value to text.

## Reference

```python
def receipt_line(item, quantity, price):
    return f"{quantity} x {item} = {quantity * price}"
```
