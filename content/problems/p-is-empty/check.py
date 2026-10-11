from solution import is_empty
from checker import case
case("empty", is_empty([]), True)
case("one item", is_empty(["bread"]), False)
case("returns a boolean", type(is_empty([])).__name__, "bool")
