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

`strip` removes spaces from both ends. Useful for cleaning up what people type.

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

## Splitting text into pieces

`split` breaks a string at spaces into a **list** of pieces, and `join` puts
pieces back together with a separator. Lists are the subject of the next
module, so for now just see what they look like:

```python
line = "apple bread milk"
print(line.split())
print("-".join(["apple", "bread"]))
```

## Try it

:::problem normalise-name

:::problem receipt-fstring

:::problem has-prefix

Next: Module 3, Collections and loops. (Coming soon.)
