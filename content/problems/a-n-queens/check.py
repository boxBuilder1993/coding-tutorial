from solution import n_queens
from checker import case

case("one", n_queens(1), 1)
case("two has no solution", n_queens(2), 0)
case("three has no solution", n_queens(3), 0)
case("four", n_queens(4), 2)
case("six", n_queens(6), 4)
case("eight", n_queens(8), 92)
case("nine", n_queens(9), 352)
