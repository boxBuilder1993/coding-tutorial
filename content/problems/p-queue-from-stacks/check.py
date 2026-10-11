from solution import drain
from checker import case
case("interleaved", drain([("add", "a"), ("add", "b"), ("take",), ("add", "c"), ("take",), ("take",)]), ["a", "b", "c"])
case("take on empty is ignored", drain([("take",), ("add", "x"), ("take",)]), ["x"])
case("all adds then all takes", drain([("add", 1), ("add", 2), ("add", 3), ("take",), ("take",), ("take",)]), [1, 2, 3])
case("adds after a partial drain keep order", drain([("add", 1), ("add", 2), ("take",), ("add", 3), ("add", 4), ("take",), ("take",), ("take",)]), [1, 2, 3, 4])
case("no operations", drain([]), [])
