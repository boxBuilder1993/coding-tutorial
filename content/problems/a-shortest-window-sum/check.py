from solution import shortest_window
from checker import case

case("classic", shortest_window([2, 3, 1, 2, 4, 3], 7), 2)
case("never reaches", shortest_window([1, 1, 1], 5), 0)
case("single item enough", shortest_window([5], 5), 1)
case("needs everything", shortest_window([1, 2, 3], 6), 3)
case("one big item", shortest_window([1, 4, 4], 4), 1)
case("empty", shortest_window([], 1), 0)
case("large", shortest_window([1] * 100000 + [1000], 1000), 1)
