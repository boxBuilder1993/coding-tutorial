from solution import positions
from checker import case
case("three matches", positions(["a", "b", "a", "c", "a"], "a"), [0, 2, 4])
case("none", positions(["a"], "z"), [])
case("empty", positions([], "a"), [])
