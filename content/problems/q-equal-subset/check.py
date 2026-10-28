from solution import can_split
from checker import case

case("classic", can_split([1, 5, 11, 5]), True)
case("impossible", can_split([1, 2, 3, 5]), False)
case("empty", can_split([]), True)
case("single", can_split([4]), False)
case("pair", can_split([3, 3]), True)
case("larger", can_split([2, 2, 3, 5, 7, 9]), True)
