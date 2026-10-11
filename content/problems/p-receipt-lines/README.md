# Receipt lines

`order` maps item names to `(quantity, price)` tuples. Write
`receipt(order)` that returns one line per item, alphabetical by item, in
the form `<item> x <quantity> = <total>`.

```static
receipt({"milk": (2, 2.5), "bread": (3, 25)})  ->  ["bread x 3 = 75", "milk x 2 = 5.0"]
```

## Starter

```python
def receipt(order):
    ...
```

## Hints

1. `sorted` over the keys, unpack the tuple, f-string.
2. `for item in sorted(order): qty, price = order[item]`

## Approach

Sort the keys, look up each tuple, unpack, format.

## Reference

```python
def receipt(order):
    lines = []
    for item in sorted(order):
        qty, price = order[item]
        lines.append(f"{item} x {qty} = {qty * price}")
    return lines
```
