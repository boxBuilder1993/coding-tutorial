# Strings: looking inside

A string is a sequence of characters, and Python lets you look at any part
of it. This page is about reading a string: its length, its characters, and
pieces of it.

## Length

`len` gives the number of characters, spaces included.

```python
item = "sourdough bread"
print(len(item))
print(len(""))
```

## Indexing

Each character has a position, starting from **0**. Square brackets pick one out.

```python
item = "bread"
print(item[0])
print(item[1])
print(item[4])
```

Positions run from 0 to `len(item) - 1`. Asking for `item[5]` here is an
`IndexError`. Negative positions count from the end: `-1` is the last
character, `-2` the one before it.

```python
item = "bread"
print(item[-1])
print(item[-2])
```

## Slicing

`item[start:stop]` gives the characters from `start` up to **but not
including** `stop`.

```python
item = "sourdough"
print(item[0:4])
print(item[4:9])
```

Leaving out `start` means "from the beginning", leaving out `stop` means
"to the end". So `item[:4]` is the first four characters and `item[4:]` is
everything after them. Slices never raise an error for going past the end;
they just stop.

```python
item = "sourdough"
print(item[:4])
print(item[4:])
print(item[-3:])
```

## Is it in there?

`in` asks whether one string appears inside another. It gives a boolean, so
it fits straight into an `if`.

```python
item = "sourdough bread"
print("bread" in item)
print("milk" in item)
print(" " in item)
```

## Joining and repeating

`+` joins strings. `*` repeats one.

```python
print("sour" + "dough")
print("-" * 20)
```

`+` only joins strings with strings. To put a number into text, convert it
with `str` first. The opposite, `int`, turns text like `"42"` into a number.

```python
total = 120
print("Total: " + str(total))
print(int("42") + 1)
```

The next page shows a nicer way to build text from values.

## Try it

:::problem first-letter

:::problem last-three

:::problem has-space

Next: [String methods](../04-string-methods).
