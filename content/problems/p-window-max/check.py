from solution import window_max
from checker import case
case("example", window_max([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
case("k is one", window_max([4, 2, 9], 1), [4, 2, 9])
case("k equals length", window_max([4, 2, 9], 3), [9])
case("decreasing", window_max([5, 4, 3, 2], 2), [5, 4, 3])
case("duplicates", window_max([2, 2, 2], 2), [2, 2])
