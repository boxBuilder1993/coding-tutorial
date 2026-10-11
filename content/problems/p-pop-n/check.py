from solution import pop_n
from checker import case
s = ["a", "b", "c"]
case("pop two", pop_n(s, 2), ["c", "b"])
case("stack shrank", s, ["a"])
t = ["a"]
case("runs out", pop_n(t, 3), ["a"])
case("stack is empty after running out", t, [])
case("pop none", pop_n(["a"], 0), [])
