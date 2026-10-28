from solution import contains
from checker import case, from_level_order, TreeNode

tree = from_level_order([8, 3, 10, 1, 6, None, 14])
case("present, deep", contains(tree, 6), True)
case("absent", contains(tree, 7), False)
case("empty", contains(None, 7), False)
case("root", contains(tree, 8), True)
case("leaf on the right", contains(tree, 14), True)
case("smaller than everything", contains(tree, 0), False)


def build(lo, hi):
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    return TreeNode(mid, build(lo, mid - 1), build(mid + 1, hi))


big = build(0, 100000)
case("a hundred thousand nodes, present", contains(big, 77777), True)
case("a hundred thousand nodes, absent", contains(big, 100001), False)
