from solution import serving_order
from checker import case
case("mixed", serving_order([("Ada", False), ("Grace", True), ("Linus", False), ("Ken", True)]), ["Grace", "Ken", "Ada", "Linus"])
case("no vips", serving_order([("a", False), ("b", False)]), ["a", "b"])
case("all vips keep order", serving_order([("a", True), ("b", True)]), ["a", "b"])
case("empty", serving_order([]), [])
