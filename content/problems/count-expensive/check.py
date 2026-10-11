from solution import count_over
from checker import case

case("two over 30", count_over([40, 25, 60, 2.5], 30), 2)
case("strictly greater", count_over([40, 25, 60, 2.5], 60), 0)
case("all over", count_over([5, 6, 7], 1), 3)
case("empty", count_over([], 10), 0)
