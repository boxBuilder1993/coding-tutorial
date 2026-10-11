# Stacks

A **stack** is a pile. You put things on the top and take things off the
top, so the last thing in is the first thing out. Undo in an editor is a
stack: each change goes on top, and undo takes the most recent one off.

Python has no separate stack type because a list already is one. `append`
puts a value on top, `pop()` takes the top value off and returns it.

```python
history = []
history.append("add bread")
history.append("add milk")
history.append("remove bread")
print(history)

last = history.pop()
print("undo:", last)
print(history)
```

Both operations work at the **end** of the list, which is fast however long
the list gets. That end is "the top".

## Looking without taking

`history[-1]` shows the top without removing it. Before popping or peeking,
check the stack is not empty: `pop` on an empty list is an error.

```python
history = ["add bread"]
print(history[-1])
print(len(history) > 0)

history.pop()
print(len(history) == 0)
```

An empty list counts as `False` in an `if`, so `if history:` means "if the
stack has anything on it" and `while history:` keeps going until it is empty.

## Reversing with a stack

Push everything on, pop everything off, and it comes out backwards. This is
the simplest thing a stack does, and the shape of every stack loop: push in
one loop, pop in another.

```python
word = "bread"
stack = []
for ch in word:
    stack.append(ch)

reversed_word = ""
while stack:
    reversed_word += stack.pop()
print(reversed_word)
```

## Matching brackets

The classic stack problem. Reading `( ( ) )` left to right, every `(` is an
open question that the next `)` answers, and the most recent open question
must be answered first. Push on `(`, pop on `)`, and the text is balanced if
nothing is left at the end and you never tried to pop from empty.

```python
text = "(()())"
stack = []
ok = True
for ch in text:
    if ch == "(":
        stack.append(ch)
    elif ch == ")":
        if not stack:
            ok = False
            break
        stack.pop()
print(ok and len(stack) == 0)
```

Try `"(()"` and `"())"` to see both ways it can fail.

## Try it

:::problem undo-last

:::problem reverse-with-stack

:::problem balanced-brackets

Next: [Queues](../02-queues).
