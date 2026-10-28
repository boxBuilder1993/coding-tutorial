from solution import min_total
from checker import case

case("classic", min_total([(10, 20), (30, 200), (400, 50), (30, 20)]), 110)
case("two people", min_total([(5, 1), (1, 5)]), 2)
case("empty", min_total([]), 0)
case("all same", min_total([(3, 3), (3, 3)]), 6)
case("harder", min_total([(259, 770), (448, 54), (926, 667), (184, 139), (840, 118), (577, 469)]), 1859)
