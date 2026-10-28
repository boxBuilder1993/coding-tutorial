from solution import max_units
from checker import case

case("classic", max_units([(1, 3), (2, 2), (3, 1)], 4), 8)
case("one type", max_units([(5, 10)], 2), 20)
case("room for everything", max_units([(1, 1), (1, 2)], 10), 3)
case("zero capacity", max_units([(1, 5)], 0), 0)
case("empty", max_units([], 5), 0)
case("ties", max_units([(2, 4), (3, 4)], 4), 16)
