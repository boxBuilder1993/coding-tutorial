from solution import combination_sum
from checker import case


def same_combos(actual, expected):
    return sorted(tuple(c) for c in actual) == sorted(tuple(c) for c in expected)


case("seven", combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]], compare=same_combos)
case("eight", combination_sum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]], compare=same_combos)
case("impossible", combination_sum([2], 1), [], compare=same_combos)
case("unsorted candidates", combination_sum([5, 2, 3], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]], compare=same_combos)
case("each combination sorted", all(c == sorted(c) for c in combination_sum([3, 2], 5)), True)
case("count for a bigger target", len(combination_sum([2, 3, 5, 7], 30)), 45)
