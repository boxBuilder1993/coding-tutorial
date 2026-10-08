# Values and print

A program is a list of instructions. Python reads them top to bottom and does
each one. The most useful instruction at the start is `print`, which shows a
value on the screen.

```python
print("Welcome to the shop")
print(42)
```

Press **Run**. Two lines appear, one per `print`. The code boxes on this site
can be edited, so change the text between the quotes and run again.

## Two kinds of value

`"Welcome to the shop"` is text. In Python, text is called a **string**, and
it is always written between quotes. `42` is a number, written without quotes.

The quotes matter. Compare these two lines:

```python
print("2 + 3")
print(2 + 3)
```

The first prints the characters `2 + 3`, because it is a string. The second
adds the numbers and prints `5`.

## Arithmetic

Numbers can be combined with the usual symbols. `*` is multiply, `/` is
divide, `**` is "to the power of".

```python
print(10 + 4)
print(10 - 4)
print(10 * 4)
print(10 / 4)
print(2 ** 10)
```

Notice `10 / 4` prints `2.5`. Dividing always gives a number with a decimal
point, even `8 / 4`, which prints `2.0`. Two more operators are worth knowing:
`//` divides and drops the remainder, `%` gives only the remainder.

```python
print(17 // 5)
print(17 % 5)
```

So 17 split into fives is 3 fives with 2 left over.

## Nothing shows unless you print

Python computes `2 + 3` here but shows nothing, because nobody asked it to.

```python
2 + 3
```

Run it: the box reports no output. Add `print(` and `)` around it and run again.

## Printing several things

`print` can take several values separated by commas. It puts a space between them.

```python
print("Total:", 2 + 3)
print("apple", "bread", "milk")
```

## Try it

:::problem print-three-lines

:::problem receipt-line

:::problem split-the-bill

Next: [Names](../02-names).
