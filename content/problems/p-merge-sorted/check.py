from solution import merge
from checker import case
case("interleaved", merge([1, 4, 9], [2, 3, 10]), [1, 2, 3, 4, 9, 10])
case("one empty", merge([], [1, 2]), [1, 2])
case("other empty", merge([1, 2], []), [1, 2])
case("both empty", merge([], []), [])
case("all of a first", merge([1, 2], [3, 4]), [1, 2, 3, 4])
case("duplicates across", merge([1, 2], [2, 3]), [1, 2, 2, 3])
a = [1, 5]
b = [0, 3]
merge(a, b)
case("first input unchanged", a, [1, 5])
case("second input unchanged", b, [0, 3])
