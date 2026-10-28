from solution import serialize, deserialize
from checker import case, from_level_order, to_level_order

for name, levels in [("classic", [1, 2, 3, None, None, 4, 5]), ("single", [7]), ("left chain", [1, 2, None, 3]), ("negatives and big", [-10, 250, -3]), ("full", [1, 2, 3, 4, 5, 6, 7])]:
    tree = from_level_order(levels)
    case("round trip: " + name, to_level_order(deserialize(serialize(tree))), levels)
case("round trip: empty", deserialize(serialize(None)), None)
case("serialize returns a string", type(serialize(from_level_order([1]))), str)
