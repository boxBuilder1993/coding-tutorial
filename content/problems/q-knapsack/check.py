from solution import best_value
from checker import case

case("classic", best_value([(1, 1), (3, 4), (4, 5), (5, 7)], 7), 9)
case("too heavy", best_value([(5, 10)], 4), 0)
case("empty", best_value([], 10), 0)
case("take everything", best_value([(1, 2), (2, 3)], 10), 5)
case("once only", best_value([(2, 10)], 6), 10)
case("harder", best_value([(10, 60), (20, 100), (30, 120)], 50), 220)
