from solution import degrees
from checker import case

case("example", degrees([("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")]), {"A": 2, "B": 2, "C": 3, "D": 1})
case("empty", degrees([]), {})
case("single edge", degrees([(1, 2)]), {1: 1, 2: 1})
case("star", degrees([(0, 1), (0, 2), (0, 3)]), {0: 3, 1: 1, 2: 1, 3: 1})
