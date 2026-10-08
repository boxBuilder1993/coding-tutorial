# Functions

So far every program runs once, top to bottom. A **function** is a set of
instructions with a name, so you can run them whenever you like, with
different values each time.

```python
def double(x):
    return x * 2

print(double(5))
print(double(21))
```

Three things to notice:

- `def double(x):` starts the function. `double` is its name, `x` is its
  **parameter**: a name for whatever value is passed in.
- The lines inside are indented by four spaces. Indentation is how Python
  knows which lines belong to the function.
- `return x * 2` hands the result back to whoever called the function.

`double(5)` is a **call**. Python sets `x` to 5, runs the body, and the call
is replaced by the returned value, 10, which `print` then shows.

## return is not print

This trips up everyone at first. `print` shows a value on the screen. `return`
gives a value back to the code that called the function. A function that
prints but does not return gives back nothing:

```python
def double_and_print(x):
    print(x * 2)

result = double_and_print(5)
print("result is", result)
```

The first line of output is `10`, from the print inside. The second says
`result is None`, because nothing was returned. `None` is Python's word for
"no value".

The exercises on this site check what your function **returns**. If a check
says it got `None`, you probably printed instead of returning.

## Several parameters

Separate parameters with commas. The values are matched up in order.

```python
def line_total(price, quantity):
    return price * quantity

print(line_total(40, 3))
print(line_total(2.5, 4))
```

## Functions can use other functions

Once a function exists, any later code can call it, including other functions.

```python
def line_total(price, quantity):
    return price * quantity

def total_with_tax(price, quantity):
    subtotal = line_total(price, quantity)
    return subtotal * 1.1

print(total_with_tax(40, 3))
```

`subtotal` here is a name that exists only inside `total_with_tax`. Names
created inside a function disappear when the function returns.

## Try it

:::problem triple

:::problem change-due

:::problem celsius-to-fahrenheit

Next: [True and False](../../02-decisions-and-text/01-true-and-false).
