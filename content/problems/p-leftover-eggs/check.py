from solution import leftover
from checker import case
case("two left", leftover(20, 6), 2)
case("none left", leftover(12, 6), 0)
case("fewer than a box", leftover(4, 6), 4)
