# Days until a warmer day

Given daily temperatures, find for each day how many days you have to
wait until a warmer one, or 0 if none comes. One way: walk the days left
to right keeping a stack of days that are still waiting for a warmer day.
When a new day arrives, pop every waiting day that is colder than it; for
each one popped, the answer is the distance between them. Then push the
new day to wait its turn. Days left on the stack at the end get 0.

Write `days_until_warmer(temps)` that returns the list of waits. Store
positions on the stack, not temperatures, since you need the distances.

```static
days_until_warmer([73, 74, 75, 71, 69, 72, 76, 73])  ->  [1, 1, 4, 2, 1, 1, 0, 0]
```

## Starter

```python
def days_until_warmer(temps):
    ...
```

## Hints

1. Start with `answer = [0] * len(temps)` and a stack of indices.
2. `while stack and temps[stack[-1]] < t: j = stack.pop(); answer[j] = i - j`, then `stack.append(i)`.

## Approach

Each day is pushed once and popped at most once. The stack always holds days in decreasing temperature order from bottom to top, which is why only the top needs checking.

## Reference

```python
def days_until_warmer(temps):
    answer = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
```
