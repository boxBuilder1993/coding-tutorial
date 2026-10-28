from solution import longest_path
from checker import case

case("classic", longest_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]]), 4)
case("second classic", longest_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]]), 4)
case("single", longest_path([[1]]), 1)
case("flat", longest_path([[2, 2], [2, 2]]), 1)
case("snake", longest_path([[1, 2, 3], [6, 5, 4], [7, 8, 9]]), 9)
big = [[(r * 50 + c) for c in range(50)] for r in range(50)]
case("fifty square increasing", longest_path(big), 99)
