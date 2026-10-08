# Values and print

A program is a list of instructions the computer follows from top to bottom.
The simplest instruction shows something on the screen. In Python that is `print`.

```python
print("Hello")
print(42)
```

Press **Run** above. The text inside the quotes is shown exactly. The number
is shown as a number. Try changing the text and running again.

## Numbers

Python can do arithmetic. `*` multiplies, `/` divides, `**` raises to a power.

```python
print(2 + 3)
print(7 * 6)
print(10 / 4)
print(2 ** 10)
```

Nothing appears unless you `print` it. This runs but shows nothing:

```python
2 + 3
```

## Names

A name lets you keep a value and use it later. The `=` sign means "give this
name this value", not "is equal to".

```python
price = 40
quantity = 3
print(price * quantity)
```

## Functions

A function is a named recipe. You give it inputs and it gives back a result
with `return`. The lines inside are indented by four spaces.

```python
def double(x):
    return x * 2

print(double(5))
print(double(21))
```

Now write one yourself.

:::problem fahrenheit

Strings can be joined with `+`.

```python
first = "Ada"
last = "Lovelace"
print(first + " " + last)
```

:::problem greet

Next: [Lists](../02-lists).
