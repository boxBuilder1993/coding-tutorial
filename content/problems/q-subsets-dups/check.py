from solution import unique_subsets
from checker import case


def same(actual, expected):
    return sorted(tuple(s) for s in actual) == sorted(tuple(s) for s in expected)


case("one repeat", unique_subsets([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], compare=same)
case("empty", unique_subsets([]), [[]], compare=same)
case("all same", unique_subsets([3, 3, 3]), [[], [3], [3, 3], [3, 3, 3]], compare=same)
case("no repeats", unique_subsets([2, 1]), [[], [1], [2], [1, 2]], compare=same)
case("count", len(unique_subsets([1, 1, 2, 2, 3])), 18)
