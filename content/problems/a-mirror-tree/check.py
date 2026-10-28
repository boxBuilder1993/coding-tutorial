from solution import mirror
from checker import case, from_level_order, to_level_order

case("example tree", to_level_order(mirror(from_level_order([8, 3, 10, 1, 6, None, 14]))), [8, 10, 3, 14, None, 6, 1])
case("empty", mirror(None), None)
case("single node", to_level_order(mirror(from_level_order([1]))), [1])
case("left chain becomes right chain", to_level_order(mirror(from_level_order([1, 2, None, 3]))), [1, None, 2, None, 3])
case("mirror twice is identity", to_level_order(mirror(mirror(from_level_order([1, 2, 3, 4, 5, 6, 7])))), [1, 2, 3, 4, 5, 6, 7])
tree = from_level_order([1, 2, 3])
case("returns the same root object", mirror(tree) is tree, True)
