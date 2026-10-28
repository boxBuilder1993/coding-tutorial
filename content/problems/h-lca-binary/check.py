from solution import lca
from checker import case, from_level_order as t

tree = t([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
case("different sides of root", lca(tree, 5, 1), 3)
case("one is the ancestor", lca(tree, 5, 4), 5)
case("deep siblings", lca(tree, 7, 4), 2)
case("cousins", lca(tree, 6, 4), 5)
case("far apart", lca(tree, 7, 8), 3)
case("order does not matter", lca(tree, 4, 7), 2)
