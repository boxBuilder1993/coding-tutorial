from solution import price_range
from checker import case
case("three", price_range([40, 2.5, 25]), (2.5, 40))
case("one", price_range([7]), (7, 7))
case("returns a tuple", type(price_range([1, 2])).__name__, "tuple")
