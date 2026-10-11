from solution import pop_n
from checker import case
s = ["a", "b", "c"]
case("pop two", pop_n(s, 2), ["c", "b"])
case("stack shrank", s, ["a"])
case("runs out", pop_n(["a"], 3), ["a"])
case("pop none", pop_n(["a"], 0), [])
