from solution import min_after
from checker import case
case("example", min_after([("push", 5), ("push", 3), ("push", 7), ("pop",), ("pop",)]), [5, 3, 3, 3, 5])
case("pop to empty", min_after([("push", 2), ("pop",)]), [2, None])
case("pop on empty ignored", min_after([("pop",), ("push", 4)]), [None, 4])
case("duplicate minimums", min_after([("push", 1), ("push", 1), ("pop",)]), [1, 1, 1])
case("decreasing pushes", min_after([("push", 9), ("push", 8), ("push", 7)]), [9, 8, 7])
