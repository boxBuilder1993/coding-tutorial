from solution import push_and_peek
from checker import case
s = ["a", "b"]
case("returns the new top", push_and_peek(s, "c"), "c")
case("the stack grew", s, ["a", "b", "c"])
case("onto empty", push_and_peek([], "x"), "x")
