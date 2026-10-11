# While loops

A `for` loop runs once per item. A `while` loop runs **as long as a condition
is true**, which is what you need when you do not know in advance how many
times to go round.

```python
stock = 2
while stock < 10:
    stock += 3
    print("Restocked to", stock)
print("Done")
```

Before each round Python checks `stock < 10`. If true, the block runs; if
false, the loop ends and the program continues after it. Here it runs three
times: 5, 8, 11.

## Counting with while

Anything `for` with `range` can do, `while` can do with a counter, though
`for` is shorter when the count is known.

```python
i = 0
while i < 3:
    print("Box", i)
    i += 1
```

The `i += 1` is essential. Without it the condition never changes.

## The infinite loop

Delete the `i += 1` line above and run it. The condition `i < 3` stays true
forever, so the loop never ends. The output box fills with "Box 0", and this
site stops the program after ten seconds. A real program would run until you
killed it.

Press **Stop** if you get tired of waiting. Every `while` loop needs something
in its body that eventually makes the condition false. When a program hangs,
that missing line is the first thing to look for.

## Leaving early with break

`break` ends the loop immediately, whatever the condition says. It is the
usual way to write "loop until something is found":

```python
prices = [40, 25, 60, 2.5]
i = 0
while i < len(prices):
    if prices[i] > 50:
        print("First expensive item is at position", i)
        break
    i += 1
```

`break` works in `for` loops too.

## Which loop?

Use `for` when you are going through items or a known number of times. Use
`while` when the number of rounds depends on what happens inside the loop:
halving until small enough, retrying until it works, reading until the end.

## Try it

:::problem restock-until-full

:::problem halve-until-under

:::problem first-over-price

Next: [Dictionaries](../05-dictionaries).
