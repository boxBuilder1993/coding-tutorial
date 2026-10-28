from solution import max_profit
from checker import case

case("classic", max_profit([(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]), 120)
case("single", max_profit([(1, 2, 5)]), 5)
case("empty", max_profit([]), 0)
case("all overlap", max_profit([(1, 5, 3), (2, 6, 5), (3, 7, 4)]), 5)
case("chain of three", max_profit([(1, 2, 1), (2, 3, 1), (3, 4, 1), (1, 4, 2)]), 3)
case("skip a big one", max_profit([(1, 4, 20), (2, 3, 15), (3, 5, 10)]), 25)
