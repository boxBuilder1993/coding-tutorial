from solution import last_occurrence
from checker import case

case("repeats", last_occurrence([1, 2, 2, 2, 3, 5], 2), 3)
case("absent", last_occurrence([1, 2, 2, 2, 3, 5], 4), -1)
case("empty", last_occurrence([], 1), -1)
case("last item", last_occurrence([1, 3, 3], 3), 2)
case("all the same", last_occurrence([7, 7, 7, 7], 7), 3)
case("single present", last_occurrence([4], 4), 0)
big = [i // 4 for i in range(10 ** 6)]
case("a million items", last_occurrence(big, 1000), 4003)
