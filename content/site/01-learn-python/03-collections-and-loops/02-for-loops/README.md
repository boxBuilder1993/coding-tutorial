# For loops

A `for` loop runs a block once for each item in a list. The name after `for`
takes each value in turn.

```python
items = ["apple", "bread", "milk"]
for item in items:
    print("Buying", item)
```

Three iterations, one per item.

## Which lines repeat?

The `for` line ends with a colon and owns a block, exactly like `def` and
`if`. Every line indented under it runs once per item. The first line that
is **not** indented is outside the loop and runs once, after the loop has
finished.

```python
items = ["apple", "bread", "milk"]
for item in items:
    print("Buying", item)
    print("...added to basket")
print("Checkout")
```

Two lines inside the loop, so six lines of output, then `Checkout` once.
Move `print("Checkout")` four spaces to the right and run again: it becomes
part of the block and prints three times.

Blocks can sit inside blocks. An `if` inside a loop is indented four spaces
further than the `for`, and its own lines four spaces further still:

```python
prices = [40, 25, 60]
for price in prices:
    if price > 30:
        print(price, "is expensive")
    print("checked", price)
print("done")
```

Read the indentation as nesting: `print(price, "is expensive")` belongs to
the `if`, which belongs to the `for`. `print("checked", price)` belongs to
the `for` only, so it runs for every price. `print("done")` belongs to
nothing and runs once.

## Accumulating a result

The most common loop shape: start with an empty result, add to it each time
round, use it at the end.

```python
prices = [40, 25, 2.5]
total = 0
for price in prices:
    total += price
print("Total:", total)
```

`total` must be created before the loop. Inside, `total += price` updates it.
The same shape counts things, builds strings, or finds the biggest value:

```python
prices = [40, 25, 60, 2.5]
biggest = prices[0]
for price in prices:
    if price > biggest:
        biggest = price
print(biggest)
```

## Looping over numbers

`range` produces a run of numbers to loop over. With one argument it starts
at 0 and stops **before** that number, so `range(3)` gives 0, 1, 2.

```python
for i in range(3):
    print(i)
```

With two arguments, the first is where to start. `range(1, 4)` gives 1, 2, 3:
it starts at 1 and still stops before 4. The same half-open rule as slicing.

```python
for i in range(1, 4):
    print("Box", i)

for year in range(2020, 2024):
    print(year)
```

A third argument is the step. `range(0, 20, 5)` gives 0, 5, 10, 15. A negative
step counts down, and then the start must be the larger number.

```python
for i in range(0, 20, 5):
    print(i)

for i in range(3, 0, -1):
    print(i)
print("Go!")
```


## Looping over the characters of a string

A string is a sequence too, so `for` walks through its characters.

```python
for ch in "bread":
    print(ch)
```

And `split`, from the string methods page, turns a sentence into a list of
words you can loop over:

```python
line = "apple bread milk"
for word in line.split():
    print(word.upper())
```

## Try it

:::problem total-price

:::problem count-expensive

:::problem longest-name

Next: [More list operations](../03-more-list-operations).
