# Names

Typing the same value over and over gets old. A **name** keeps a value so you
can use it again. You create one with `=`.

```python
price = 40
print(price)
print(price * 3)
```

`price = 40` means "from now on, `price` refers to 40". It does not mean
"price is equal to 40" in the maths sense. The value is on the right, the
name on the left, always.

## Names can change

Assigning again replaces the old value.

```python
stock = 10
print(stock)
stock = 7
print(stock)
```

The second `print` shows `7`. The old value is gone.

A very common pattern is to update a name using its own current value:

```python
stock = 10
stock = stock - 1
print(stock)
```

Read `stock = stock - 1` right to left: compute `stock - 1`, which is 9, then
make `stock` refer to 9. Python has a shortcut for this: `stock -= 1`. The
same works for `+=`, `*=` and `/=`.

## Names for strings

Any value can be named, including text.

```python
item = "bread"
print(item)
print("You bought", item)
```

## Choosing names

Names are made of letters, digits and underscores, and cannot start with a
digit. Python is case sensitive: `Price` and `price` are different names.
Use names that say what the value is. `unit_price` beats `x`.

Using a name before it exists is an error. Run this and read the message:

```python
print(total)
```

`NameError: name 'total' is not defined` means exactly what it says: there is
no name `total` yet. You will see this error often. It almost always means a
typo or a forgotten line.

## Try it

:::problem name-and-print

:::problem update-stock

:::problem swap-names

Next: [Functions](../03-functions).
