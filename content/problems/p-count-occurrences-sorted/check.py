from solution import count_sorted
from checker import case
case("three", count_sorted([1, 2, 2, 2, 3, 5], 2), 3)
case("absent in the middle", count_sorted([1, 3], 2), 0)
case("empty", count_sorted([], 1), 0)
case("all equal", count_sorted([4, 4, 4], 4), 3)
case("at the start", count_sorted([1, 1, 2], 1), 2)
case("at the end", count_sorted([1, 2, 2], 2), 2)
case("below all", count_sorted([5, 6], 1), 0)
case("above all", count_sorted([5, 6], 9), 0)
