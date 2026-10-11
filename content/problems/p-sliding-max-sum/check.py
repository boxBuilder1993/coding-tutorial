from solution import best_window
from checker import case
case("example", best_window([2, 1, 5, 1, 3, 2], 3), 9)
case("k equals length", best_window([1, 2, 3], 3), 6)
case("k is one", best_window([4, 9, 2], 1), 9)
case("negatives", best_window([-5, -2, -8, -1], 2), -7)
