---
title: Python string methods: upper, strip, replace, split, f-strings and format specs
description: Everyday Python string methods, why strings cannot change in place, f-strings and format specs like :.2f, and a first look at split and join.
---
# String methods

Strings come with built-in operations called **methods**. You call a method
with a dot after the value: `item.upper()`. The parentheses are required even
when there is nothing to pass.

```python
item = "Sourdough Bread"
print(item.upper())
print(item.lower())
print(item)
```

The last line shows the original is unchanged. Strings cannot be modified;
every method **returns a new string**. If you want to keep the result, name it:
`item = item.lower()`.

## The methods you will use most

```python
item = "  bread  "
print(item.strip())
```

`strip` removes spaces from both ends, and other blank characters such as
tabs and line breaks. Useful for cleaning up what people type.

```python
item = "sourdough bread"
print(item.replace("bread", "loaf"))
print(item.count("o"))
print(item.find("bread"))
print(item.find("milk"))
```

`replace` swaps every occurrence. `count` counts them. `find` gives the
position of the first match, or `-1` if there is none.

```python
code = "SKU-1042"
print(code.startswith("SKU"))
print(code.endswith("42"))
```

`startswith` and `endswith` return booleans, so they slot into `if` directly.

## Building text from values

Earlier you built text with `+` and `str()`. An **f-string** is easier: put
`f` before the opening quote, and write names or expressions inside curly
braces.

```python
item = "bread"
quantity = 3
price = 40
print(f"{quantity} x {item} = {quantity * price}")
```

Anything inside `{}` is evaluated and converted to text for you. This is the
way to build output from now on.

## Controlling how numbers look

A price of `2.5` should print as `2.50`, and a column of prices should line
up. A **format spec** after a colon inside the braces does this:

```python
price = 2.5
print(f"{price:.2f}")
print(f"{1250:,}")
print(f"{0.256:.1%}")
```

`.2f` means "a decimal number with 2 digits after the point". `,` puts
thousands separators in. `.1%` multiplies by a hundred and adds the sign.
They combine: `{1250.5:,.2f}` gives `1,250.50`.

A number before the type sets a minimum width, and `<`, `>` or `^` push the
value to the left, right or centre of it. That is how you line up columns:

```python
items = ["apple", "bread", "milk"]
prices = [40, 25, 2.5]
for i in range(3):
    print(f"{items[i]:<8}{prices[i]:>8.2f}")
```

`{items[i]:<8}` is the item padded with spaces to 8 characters, left
aligned; `{prices[i]:>8.2f}` is the price with two decimals, right aligned
in 8 characters. You will not remember all of these. Remember that `.2f`
exists and that the colon is where the rest goes.

## Splitting text into pieces

`split()` breaks a string into a **list** of pieces wherever there is blank
space, treating any run of spaces as one break. Give it a separator, like
`split("-")`, to break at that character instead. `join` puts pieces back
together with a separator. Lists are the subject of the next module, so for
now just see what they look like:

```python
line = "apple  bread milk"
print(line.split())
print("BRD-001-A".split("-"))
print("-".join(["apple", "bread"]))
```

## Try it

:::problem normalise-name

:::problem receipt-fstring

:::problem money-format

:::problem has-prefix

Next: [Lists](../../03-collections-and-loops/01-lists).
