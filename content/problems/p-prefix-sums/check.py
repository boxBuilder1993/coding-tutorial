from solution import range_sums
from checker import case
case("example", range_sums([2, 4, 6, 8], [(0, 1), (1, 3), (2, 2)]), [6, 18, 6])
case("whole list", range_sums([1, 2, 3], [(0, 2)]), [6])
case("no queries", range_sums([1, 2], []), [])
case("negatives", range_sums([5, -3, 2], [(0, 1), (1, 2)]), [2, -1])
