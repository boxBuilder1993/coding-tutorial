from solution import stock_value
from checker import case
case("one unpriced", stock_value({"apple": 3, "bread": 2, "gift": 1}, {"apple": 40, "bread": 25}), 170)
case("no prices", stock_value({"apple": 3}, {}), 0)
case("empty stock", stock_value({}, {"apple": 40}), 0)
