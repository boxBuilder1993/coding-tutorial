from collections import deque
from solution import rotate
from checker import case
case("once", list(rotate(deque(["a", "b", "c"]), 1)), ["b", "c", "a"])
case("wraps around", list(rotate(deque(["a", "b", "c"]), 4)), ["b", "c", "a"])
case("zero", list(rotate(deque(["a", "b"]), 0)), ["a", "b"])
case("empty", list(rotate(deque(), 3)), [])
