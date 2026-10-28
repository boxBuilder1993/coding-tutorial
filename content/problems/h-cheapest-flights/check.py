from solution import cheapest
from checker import case

case("one stop", cheapest(4, [(0, 1, 100), (1, 2, 100), (2, 0, 100), (1, 3, 600), (2, 3, 200)], 0, 3, 1), 700)
case("stop allowed", cheapest(3, [(0, 1, 100), (1, 2, 100), (0, 2, 500)], 0, 2, 1), 200)
case("no stops", cheapest(3, [(0, 1, 100), (1, 2, 100), (0, 2, 500)], 0, 2, 0), 500)
case("impossible", cheapest(3, [(0, 1, 100)], 0, 2, 5), -1)
case("same city", cheapest(2, [(0, 1, 5)], 0, 0, 0), 0)
case("more stops, cheaper", cheapest(5, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (0, 4, 10)], 0, 4, 3), 4)
case("too few stops for the cheap path", cheapest(5, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (0, 4, 10)], 0, 4, 2), 10)
