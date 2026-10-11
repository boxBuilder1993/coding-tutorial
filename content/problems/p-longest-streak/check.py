from solution import longest_streak
from checker import case
case("middle streak", longest_streak([5, 12, 14, 3, 10, 11, 15], 10), 3)
case("none", longest_streak([1, 2], 10), 0)
case("all", longest_streak([10, 10, 10], 10), 3)
case("streak at the end", longest_streak([1, 10, 1, 10, 10], 10), 2)
case("empty", longest_streak([], 1), 0)
