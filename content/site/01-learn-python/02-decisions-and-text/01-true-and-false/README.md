# True and False

Programs constantly ask questions. Is the stock empty? Is the order big
enough for free delivery? Python answers every such question with one of two
values: `True` or `False`.

```python
print(10 > 3)
print(10 < 3)
print(10 == 10)
```

`True` and `False` are values like `42` or `"bread"`. They are called
**booleans**. You can print them, name them, and return them from functions.

## Comparisons

| Written | Meaning |
|---------|---------|
| `a == b` | equal |
| `a != b` | not equal |
| `a < b`, `a > b` | less than, greater than |
| `a <= b`, `a >= b` | less than or equal, greater than or equal |

Equality uses **two** equals signs. One `=` gives a name a value; two `==`
ask whether two values are the same. Mixing them up is the most common
mistake at this stage.

```python
stock = 0
print(stock == 0)
print(stock != 0)
```

Comparisons work on text too. `==` checks the text matches exactly, including
capital letters.

```python
item = "Bread"
print(item == "bread")
print(item == "Bread")
```

## Combining questions

`and` is true only if both sides are true. `or` is true if either side is.
`not` flips a boolean.

```python
quantity = 3
price = 40

print(quantity > 0 and price < 50)
print(quantity > 5 or price < 50)
print(not quantity > 0)
```

Read `quantity > 0 and price < 50` as "quantity is positive and price is
under 50". Python checks each side, then combines them.

## Functions that answer questions

A function can return a boolean. By convention their names read like a
question: `is_empty`, `has_discount`, `can_deliver`.

```python
def is_in_stock(quantity):
    return quantity > 0

print(is_in_stock(5))
print(is_in_stock(0))
```

There is no `if` here. `quantity > 0` already is `True` or `False`, so it is
returned directly.

## Try it

:::problem is-free-delivery

:::problem is-valid-quantity

:::problem same-item

Next: [Making decisions](../02-making-decisions).
