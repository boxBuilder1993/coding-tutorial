from solution import content_children
from checker import case

case("not enough big biscuits", content_children([1, 2, 3], [1, 1]), 1)
case("everyone content", content_children([1, 2], [1, 2, 3]), 2)
case("no children", content_children([], [1]), 0)
case("no biscuits", content_children([1], []), 0)
case("unsorted input", content_children([3, 1, 2], [2, 3, 1]), 3)
case("one huge biscuit", content_children([5, 5], [10]), 1)
a, b = [3, 1], [2, 4]
content_children(a, b)
case("does not change the inputs", (a, b), ([3, 1], [2, 4]))
