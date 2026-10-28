from solution import merge_into
from checker import case

case("classic", merge_into([1, 2, 3, 0, 0, 0], 3, [2, 5, 6]), [1, 2, 2, 3, 5, 6])
case("a empty", merge_into([0], 0, [1]), [1])
case("b goes first", merge_into([2, 0], 1, [1]), [1, 2])
case("b empty", merge_into([1, 2], 2, []), [1, 2])
case("b all larger", merge_into([1, 0, 0], 1, [2, 3]), [1, 2, 3])
a = [4, 5, 6, 0, 0, 0]
result = merge_into(a, 3, [1, 2, 3])
case("same list object", result is a and a == [1, 2, 3, 4, 5, 6], True)
