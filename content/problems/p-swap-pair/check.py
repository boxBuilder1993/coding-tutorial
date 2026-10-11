from solution import swap
from checker import case
case("pair", swap(("bread", 25)), (25, "bread"))
case("numbers", swap((1, 2)), (2, 1))
case("returns a tuple", type(swap((1, 2))).__name__, "tuple")
