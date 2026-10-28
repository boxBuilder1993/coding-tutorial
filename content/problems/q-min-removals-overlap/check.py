from solution import min_removals
from checker import case

case("one removal", min_removals([(1, 2), (2, 3), (3, 4), (1, 3)]), 1)
case("duplicates", min_removals([(1, 2), (1, 2), (1, 2)]), 2)
case("touching is fine", min_removals([(1, 2), (2, 3)]), 0)
case("empty", min_removals([]), 0)
case("one long covers many", min_removals([(1, 10), (2, 3), (4, 5), (6, 7)]), 1)
