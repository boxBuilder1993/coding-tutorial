from solution import min_largest_sum
from checker import case

case("classic", min_largest_sum([7, 2, 5, 10, 8], 2), 18)
case("ascending", min_largest_sum([1, 2, 3, 4, 5], 2), 9)
case("one per piece", min_largest_sum([1, 4, 4], 3), 4)
case("single piece", min_largest_sum([3, 1, 2], 1), 6)
case("zeros", min_largest_sum([0, 0, 5], 2), 5)
case("a thousand items", min_largest_sum(list(range(1, 1001)), 7), 71766)
