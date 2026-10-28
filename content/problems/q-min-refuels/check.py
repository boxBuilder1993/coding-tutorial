from solution import min_refuels
from checker import case

case("classic", min_refuels(100, 10, [(10, 60), (20, 30), (30, 30), (60, 40)]), 2)
case("no stops needed", min_refuels(1, 1, []), 0)
case("cannot reach first station", min_refuels(100, 1, [(10, 100)]), -1)
case("one stop", min_refuels(100, 50, [(25, 50)]), 1)
case("needs every station", min_refuels(30, 10, [(10, 10), (20, 10)]), 2)
case("skipped small station", min_refuels(100, 20, [(10, 5), (20, 80)]), 1)
