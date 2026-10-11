from solution import merge_into
from checker import case
case("example", merge_into([1, 3, 5, 0, 0], 3, [2, 4]), [1, 2, 3, 4, 5])
case("b all smaller", merge_into([4, 5, 0, 0], 2, [1, 2]), [1, 2, 4, 5])
case("b all larger", merge_into([1, 2, 0, 0], 2, [3, 4]), [1, 2, 3, 4])
case("a empty", merge_into([0, 0], 0, [1, 2]), [1, 2])
case("b empty", merge_into([1, 2], 2, []), [1, 2])
case("equal values across the lists", merge_into([2, 2, 0, 0], 2, [2, 2]), [2, 2, 2, 2])
case("negatives and a real zero", merge_into([-1, 0, 0], 2, [-2]), [-2, -1, 0])
a = [1, 0]
result = merge_into(a, 1, [0])
case("same list object", result is a, True)
case("that list now holds the merge", a, [0, 1])
