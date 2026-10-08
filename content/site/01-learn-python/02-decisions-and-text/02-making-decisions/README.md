# Making decisions

A boolean on its own only reports. `if` lets the program **act** on it: run
some lines only when a condition is true.

```python
stock = 0

if stock == 0:
    print("Sold out")

print("Done")
```

The `if` line ends with a colon. The lines indented under it are the
**block**, and they run only when the condition is `True`. `print("Done")` is
not indented, so it is not part of the block and always runs. Change `stock`
to 5 and run again: "Sold out" disappears, "Done" stays.

## Otherwise

`else` gives the other path. Exactly one of the two blocks runs.

```python
order_total = 60

if order_total >= 50:
    print("Free delivery")
else:
    print("Delivery costs 5")
```

## More than two paths

`elif` is short for "else if". Python checks each condition from the top and
runs the first block whose condition is true, then skips the rest.

```python
quantity = 12

if quantity >= 10:
    print("Bulk discount")
elif quantity >= 5:
    print("Small discount")
else:
    print("No discount")
```

With `quantity = 12`, both `quantity >= 10` and `quantity >= 5` are true, but
only the first block runs. Order matters: if the `>= 5` check came first, the
bulk discount could never be reached.

## Returning from inside an if

Inside a function, `return` ends the function immediately. That makes a
common shape very clean:

```python
def delivery_fee(order_total):
    if order_total >= 50:
        return 0
    return 5

print(delivery_fee(60))
print(delivery_fee(20))
```

No `else` is needed. If the `if` returns, the second `return` is never
reached; if it does not, the function falls through to it.

## Try it

:::problem delivery-fee

:::problem discount-rate

:::problem clamp-quantity

Next: [Strings: looking inside](../03-strings-looking-inside).
