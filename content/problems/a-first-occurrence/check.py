from solution import first_occurrence
from checker import case

case("repeats in the middle", first_occurrence([1, 2, 2, 2, 3, 5], 2), 1)
case("absent", first_occurrence([1, 2, 2, 2, 3, 5], 4), -1)
case("empty", first_occurrence([], 4), -1)
case("first item", first_occurrence([2, 2, 3], 2), 0)
case("last item, single", first_occurrence([1, 3, 7], 7), 2)
case("all the same", first_occurrence([5, 5, 5, 5], 5), 0)
case("single item present", first_occurrence([9], 9), 0)
case("single item absent", first_occurrence([9], 1), -1)
big = [i // 3 for i in range(10 ** 6)]
case("a million items", first_occurrence(big, 123456), 370368)
