from solution import max_score
from checker import case

case("all equal", max_score([10, 10, 10, 10, 10], 5), 50)
case("same pile repeatedly", max_score([1, 10, 3, 3, 3], 3), 18)
case("single pile", max_score([8], 4), 8 + 4 + 2 + 1)
case("zero picks", max_score([5, 6], 0), 0)
case("odd halving", max_score([7], 3), 7 + 4 + 2)
