from solution import permutations
from checker import case


def same_lists(actual, expected):
    return sorted(tuple(p) for p in actual) == sorted(tuple(p) for p in expected)


case("three items", permutations([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], compare=same_lists)
case("empty", permutations([]), [[]], compare=same_lists)
case("one item", permutations(["x"]), [["x"]], compare=same_lists)
case("two items", permutations(["a", "b"]), [["a", "b"], ["b", "a"]], compare=same_lists)
case("count for six items", len(permutations(list(range(6)))), 720)
case("no duplicates among results", len({tuple(p) for p in permutations([1, 2, 3, 4])}), 24)
