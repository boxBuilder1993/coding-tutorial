from solution import max_product
from checker import case

case("classic", max_product([2, 3, -2, 4]), 6)
case("zero wins", max_product([-2, 0, -1]), 0)
case("two negatives", max_product([-2, 3, -4]), 24)
case("single negative", max_product([-5]), -5)
case("zeros split runs", max_product([2, 0, 3, 4, 0, 1]), 12)
case("three negatives", max_product([-1, -2, -3]), 6)
