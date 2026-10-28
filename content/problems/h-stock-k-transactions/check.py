from solution import max_profit
from checker import case

case("one trade possible", max_profit([2, 4, 1], 2), 2)
case("two trades", max_profit([3, 2, 6, 5, 0, 3], 2), 7)
case("falling market", max_profit([7, 6, 4, 3, 1], 1), 0)
case("zero trades", max_profit([1, 5], 0), 0)
case("empty", max_profit([], 3), 0)
case("one trade best over two rises", max_profit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 2), 13)
case("unlimited effectively", max_profit([1, 2, 1, 2, 1, 2], 10), 3)
