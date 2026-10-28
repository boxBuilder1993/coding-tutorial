from solution import longest_consecutive
from checker import case

case("classic", longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
case("nine long with a repeat", longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
case("empty", longest_consecutive([]), 0)
case("single", longest_consecutive([7]), 1)
case("no runs", longest_consecutive([10, 20, 30]), 1)
case("negatives", longest_consecutive([-1, 0, 1, 5]), 3)
big = list(range(0, 200000, 2)) + list(range(500001, 550000))
case("large", longest_consecutive(big), 49999)
