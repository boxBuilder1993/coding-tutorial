---
title: How a Python program runs: memory, names and the processor
description: A simple picture of what happens when Python runs your code: values on shelves, names as labels, and a processor stepping one line at a time.
---
# How a program runs

You have written a few programs now. This page is a short pause to build
a picture of what the computer is doing with them. You will not need any
hardware knowledge, and there is nothing to memorise. The picture just
makes the next few pages, and a lot of future errors, make sense.

## Two parts

For our purposes a computer has two parts that matter.

**Memory** is where values live while a program runs. Think of it as a
huge set of shelves. When your program says `price = 40`, Python puts the
value 40 on a free shelf and sticks a label on it that reads `price`.

The **processor** is the part that does things. It reads your program one
instruction at a time, starting from the top, does exactly what that
instruction says, and moves on. It never stops to wonder what you meant.
(Soon you will meet lines that send it somewhere else, such as calling a
function or repeating a loop. Even then it only ever does one instruction
at a time.)

Everything you have seen so far is these two parts working together: the
processor steps through your lines, and each line puts values on shelves,
reads values off shelves, or shows a value on the screen.

## Names are labels, not shelves

This is the one idea on the page worth slowing down for. A name does not
*contain* a value. It *points at* one. Run this:

```python
price = 40
print(price)
price = 45
print(price)
```

On the first line, 40 goes on a shelf and the `price` label is attached to
it. On the third line, 45 goes on a different shelf, and the label is
**moved** to point at the new one. Nobody refers to the old 40 any more,
so Python is free to reuse that shelf.

The same thing happens with `price = price + 5`: the processor reads the
value `price` points at, adds 5, puts the result on a new shelf, and moves
the label. The name on the left and the name on the right are the same
label at two moments in time.

Why does this matter? Because two labels can point at the same shelf. With
numbers and text you will never notice, since those values cannot be
changed once made. Later you will meet values that *can* be changed in
place, and then two labels on one shelf is a surprise waiting to happen.
When you get there, come back to this picture.

## Why order matters

Because the processor does one line at a time and never looks ahead, a name
has to be given a value *before* the line that uses it runs. Run this:

```python expect-error
print(total)
total = 100
```

The processor reaches `print(total)`, looks for a shelf labelled `total`,
finds none, and stops with a `NameError`. The assignment on the next line
is no help; the processor has not got there yet. Swap the two lines and it
works.

## Why it never gets bored

A processor carries out hundreds of millions of instructions every second.
That is the whole reason programming is worth doing: a few lines that work
once will work a million times, and the computer will not get tired or
make a mistake on the ten-thousandth repeat.

It also never gets bored, which is a problem when you tell it to repeat
forever. Later, in the section on loops, you will write a program that never
finishes, on purpose, and this site will stop it after ten seconds. That
is not the processor failing. It is the processor doing exactly what it
was told.

## What this page is not

There is a lot more to a real computer: how values are stored as electrical
states, what happens when memory runs out, how several programs share one
processor. None of it changes anything on the pages ahead, so none of it is
here. The shelves-and-stepper picture is enough to carry you through this
whole course.

Next: [Functions](../04-functions).
