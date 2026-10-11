# Evaluate a postfix expression

In postfix notation the operator comes after its two operands: `3 4 +`
means 3 + 4, and `3 4 + 2 *` means (3 + 4) * 2. It can be evaluated with
a stack in one pass: read the tokens left to right; push every number;
when you meet an operator, pop two numbers, apply the operator with the
first-popped as the right-hand operand, and push the result. At the end
the stack holds exactly one number, the answer.

Write `evaluate(expression)` for a space-separated expression using
integers and the operators `+`, `-`, `*`. The expression is always valid.

```static
evaluate("3 4 +")       ->  7
evaluate("3 4 + 2 *")   ->  14
evaluate("10 2 3 * -")  ->  4
```

## Starter

```python
def evaluate(expression):
    ...
```

## Hints

1. `split`, then for each token: operator or number? Numbers are pushed with `int`.
2. On an operator: `b = stack.pop(); a = stack.pop()` then push `a - b` for `-`. Order matters.

## Approach

Pop order is the trap: the second value popped is the left operand. `10 2 3 * -` pops 6 then 10 and computes 10 - 6.

## Reference

```python
def evaluate(expression):
    stack = []
    for token in expression.split():
        if token in "+-*":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            else:
                stack.append(a * b)
        else:
            stack.append(int(token))
    return stack[0]
```
