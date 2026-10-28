from solution import lca
from checker import case, from_level_order as t

tree = t([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
case("different sides", lca(tree, 2, 8), 6)
case("ancestor is one of them", lca(tree, 2, 4), 2)
case("deep", lca(tree, 3, 5), 4)
case("both leaves far apart", lca(tree, 0, 5), 2)
case("order does not matter", lca(tree, 9, 7), 8)
