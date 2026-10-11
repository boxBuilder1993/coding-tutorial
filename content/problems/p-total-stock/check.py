from solution import total_stock
from checker import case
case("two items", total_stock({"apple": 10, "bread": 3}), 13)
case("empty", total_stock({}), 0)
case("one", total_stock({"milk": 7}), 7)
