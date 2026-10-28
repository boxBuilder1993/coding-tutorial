from solution import count_pairs
from checker import case

case("three pairs", count_pairs([1, 5, 7, -1, 5], 6), 3)
case("all ones", count_pairs([1, 1, 1, 1], 2), 6)
case("none", count_pairs([1, 2, 3], 10), 0)
case("empty", count_pairs([], 0), 0)
case("zero target with negatives", count_pairs([-2, 2, 0, 0], 0), 2)
big = [i % 1000 for i in range(100000)]
case("a hundred thousand", count_pairs(big, 999), 100 * 100 * 500)
