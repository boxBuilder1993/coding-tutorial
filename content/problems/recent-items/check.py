from solution import last_n
from checker import case

case("last two", last_n(["apple", "bread", "milk", "eggs"], 2), ["milk", "eggs"])
case("fewer than n", last_n(["apple"], 3), ["apple"])
case("exactly n", last_n([1, 2, 3], 3), [1, 2, 3])
case("n is zero", last_n([1, 2, 3], 0), [])
case("returns a list", type(last_n([1], 1)).__name__, "list")
