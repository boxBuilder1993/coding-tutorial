from solution import merge_all
from checker import case
case("example", merge_all([[1, 4, 9], [2, 3], [], [5]]), [1, 2, 3, 4, 5, 9])
case("all empty", merge_all([[], []]), [])
case("no lists", merge_all([]), [])
case("one list", merge_all([[1, 2, 3]]), [1, 2, 3])
case("duplicates across lists", merge_all([[1, 2], [2, 3], [2]]), [1, 2, 2, 2, 3])
