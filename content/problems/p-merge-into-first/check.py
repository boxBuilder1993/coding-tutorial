from solution import merge_into
from checker import case
case("example", merge_into([1, 3, 5, 0, 0], 3, [2, 4]), [1, 2, 3, 4, 5])
case("b all smaller", merge_into([4, 5, 0, 0], 2, [1, 2]), [1, 2, 4, 5])
case("b all larger", merge_into([1, 2, 0, 0], 2, [3, 4]), [1, 2, 3, 4])
case("a empty", merge_into([0, 0], 0, [1, 2]), [1, 2])
case("b empty", merge_into([1, 2], 2, []), [1, 2])
a = [1, 0]
case("same list object", merge_into(a, 1, [0]) is a, True)
