from solution import can_reach_end
from checker import case

case("reachable", can_reach_end([2, 3, 1, 1, 4]), True)
case("stuck on a zero", can_reach_end([3, 2, 1, 0, 4]), False)
case("single item", can_reach_end([0]), True)
case("zero at the start of a longer list", can_reach_end([0, 1]), False)
case("big first jump", can_reach_end([5, 0, 0, 0, 0, 0]), True)
case("exactly enough", can_reach_end([1, 1, 1, 1]), True)
big = [1] * 100000
case("a hundred thousand ones", can_reach_end(big), True)
