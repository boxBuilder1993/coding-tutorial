from collections import deque
from solution import rotate
from checker import case
case("once", list(rotate(deque(["a", "b", "c"]), 1)), ["b", "c", "a"])
case("full turn", list(rotate(deque(["a", "b", "c"]), 3)), ["a", "b", "c"])
case("wraps around", list(rotate(deque(["a", "b", "c"]), 4)), ["b", "c", "a"])
case("more than two turns", list(rotate(deque(["a", "b", "c"]), 7)), ["b", "c", "a"])
case("zero", list(rotate(deque(["a", "b"]), 0)), ["a", "b"])
case("empty", list(rotate(deque(), 3)), [])
line = deque([1, 2])
case("same deque is returned", rotate(line, 1) is line, True)
