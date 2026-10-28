from solution import combinations
from checker import case


def same(actual, expected):
    return sorted(tuple(c) for c in actual) == sorted(tuple(c) for c in expected)


case("four choose two", combinations(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], compare=same)
case("all of them", combinations(3, 3), [[1, 2, 3]], compare=same)
case("choose none", combinations(3, 0), [[]], compare=same)
case("choose one", combinations(3, 1), [[1], [2], [3]], compare=same)
case("count twelve choose five", len(combinations(12, 5)), 792)
