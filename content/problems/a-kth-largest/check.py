from solution import kth_largest
from checker import case

case("second largest", kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
case("with repeats", kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
case("k is 1", kth_largest([7, 9, 8], 1), 9)
case("k is the length", kth_largest([7, 9, 8], 3), 7)
case("all the same", kth_largest([4, 4, 4], 2), 4)
case("single", kth_largest([42], 1), 42)
big = [(i * 7919) % 100003 for i in range(100000)]
case("a hundred thousand", kth_largest(big, 500), sorted(big, reverse=True)[499])
