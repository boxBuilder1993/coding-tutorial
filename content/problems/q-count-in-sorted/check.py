from solution import count_sorted
from checker import case

case("three twos", count_sorted([1, 2, 2, 2, 3, 5], 2), 3)
case("absent", count_sorted([1, 2, 3], 4), 0)
case("empty", count_sorted([], 1), 0)
case("everything", count_sorted([9, 9, 9], 9), 3)
case("absent in the middle", count_sorted([1, 3, 5], 4), 0)
big = [i // 100 for i in range(10 ** 6)]
case("ten thousand queries on a million items", sum(count_sorted(big, t) for t in range(0, 10000)), 10 ** 6)
