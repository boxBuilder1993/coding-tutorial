from solution import unique_permutations
from checker import case


def same(actual, expected):
    return sorted(tuple(p) for p in actual) == sorted(tuple(p) for p in expected)


case("one pair", unique_permutations([1, 1, 2]), [[1, 1, 2], [1, 2, 1], [2, 1, 1]], compare=same)
case("empty", unique_permutations([]), [[]], compare=same)
case("all same", unique_permutations([2, 2]), [[2, 2]], compare=same)
case("no repeats", len(unique_permutations([1, 2, 3])), 6)
case("count aabbb", len(unique_permutations(list("aabbb"))), 10)
