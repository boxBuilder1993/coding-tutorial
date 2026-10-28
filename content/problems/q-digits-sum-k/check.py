from solution import digit_combos
from checker import case


def same(actual, expected):
    return sorted(tuple(c) for c in actual) == sorted(tuple(c) for c in expected)


case("one answer", digit_combos(3, 7), [[1, 2, 4]], compare=same)
case("three answers", digit_combos(3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]], compare=same)
case("impossible", digit_combos(4, 1), [], compare=same)
case("all digits", digit_combos(9, 45), [[1, 2, 3, 4, 5, 6, 7, 8, 9]], compare=same)
case("count", len(digit_combos(4, 20)), 12)
