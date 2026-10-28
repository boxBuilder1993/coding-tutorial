from solution import can_partition
from checker import case

case("classic", can_partition([4, 3, 2, 3, 5, 2, 1], 4), True)
case("impossible", can_partition([1, 2, 3, 4], 3), False)
case("k is 1", can_partition([2, 2], 1), True)
case("one per group", can_partition([5, 5, 5], 3), True)
case("too big a number", can_partition([10, 1, 1], 2), False)
case("sixteen numbers into four", can_partition([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 4), True)
case("sum not divisible", can_partition([1, 1, 1], 2), False)
