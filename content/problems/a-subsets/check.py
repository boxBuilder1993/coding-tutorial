from solution import subsets
from checker import case


def same_sets(actual, expected):
    return sorted(tuple(sorted(s)) for s in actual) == sorted(tuple(sorted(s)) for s in expected)


case("two items", subsets([1, 2]), [[], [1], [2], [1, 2]], compare=same_sets)
case("empty input", subsets([]), [[]], compare=same_sets)
case("one item", subsets(["a"]), [[], ["a"]], compare=same_sets)
case("three items", subsets([1, 2, 3]), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]], compare=same_sets)
case("count for ten items", len(subsets(list(range(10)))), 1024)
result = subsets([1, 2])
case("each subset is its own list", len({id(s) for s in result}), 4)
