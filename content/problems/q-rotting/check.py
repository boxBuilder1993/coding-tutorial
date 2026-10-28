from solution import minutes_to_rot
from checker import case

case("four minutes", minutes_to_rot([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)
case("unreachable", minutes_to_rot([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1)
case("nothing fresh", minutes_to_rot([[0, 2]]), 0)
case("no oranges at all", minutes_to_rot([[0]]), 0)
case("two sources", minutes_to_rot([[2, 1, 1, 1, 2]]), 2)
case("fresh with no rotten", minutes_to_rot([[1]]), -1)
