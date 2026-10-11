from solution import cheapest_price
from checker import case
case("three", cheapest_price({"apple": 40, "milk": 2.5, "bread": 25}), 2.5)
case("one", cheapest_price({"x": 9}), 9)
case("not the key", cheapest_price({"a": 100, "z": 1}), 1)
