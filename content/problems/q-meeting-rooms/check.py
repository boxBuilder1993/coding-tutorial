from solution import rooms_needed
from checker import case

case("two rooms", rooms_needed([(0, 30), (5, 10), (15, 20)]), 2)
case("one room", rooms_needed([(7, 10), (2, 4)]), 1)
case("empty", rooms_needed([]), 0)
case("back to back", rooms_needed([(1, 2), (2, 3)]), 1)
case("all overlap", rooms_needed([(1, 5), (2, 5), (3, 5)]), 3)
case("nested", rooms_needed([(1, 10), (2, 3), (4, 5)]), 2)
