from solution import combos_once
from checker import case


def same(actual, expected):
    return sorted(tuple(c) for c in actual) == sorted(tuple(c) for c in expected)


case("classic", combos_once([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], compare=same)
case("repeats", combos_once([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]], compare=same)
case("impossible", combos_once([2, 4], 5), [], compare=same)
case("no reuse", combos_once([3], 6), [], compare=same)
case("empty candidates", combos_once([], 1), [], compare=same)
