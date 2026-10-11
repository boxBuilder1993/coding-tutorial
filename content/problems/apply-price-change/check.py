from solution import set_price
from checker import case

case("adds a new item", set_price({"apple": 40}, "bread", 25), {"apple": 40, "bread": 25})
case("replaces an existing price", set_price({"apple": 40}, "apple", 45), {"apple": 45})
case("from empty", set_price({}, "milk", 2.5), {"milk": 2.5})
original = {"apple": 40}
set_price(original, "bread", 25)
case("changes the dictionary in place", original, {"apple": 40, "bread": 25})
