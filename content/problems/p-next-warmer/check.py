from solution import days_until_warmer
from checker import case
case("example", days_until_warmer([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
case("rising", days_until_warmer([30, 40, 50]), [1, 1, 0])
case("falling", days_until_warmer([50, 40, 30]), [0, 0, 0])
case("equal is not warmer", days_until_warmer([50, 50, 51]), [2, 1, 0])
case("single", days_until_warmer([99]), [0])
case("empty", days_until_warmer([]), [])
