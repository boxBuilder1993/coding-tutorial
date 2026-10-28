from solution import largest_rectangle
from checker import case

case("classic", largest_rectangle([2, 1, 5, 6, 2, 3]), 10)
case("two bars", largest_rectangle([2, 4]), 4)
case("empty", largest_rectangle([]), 0)
case("flat", largest_rectangle([3, 3, 3]), 9)
case("ascending", largest_rectangle([1, 2, 3, 4, 5]), 9)
case("descending", largest_rectangle([5, 4, 3, 2, 1]), 9)
case("valley", largest_rectangle([6, 2, 5, 4, 5, 1, 6]), 12)
case("large", largest_rectangle([1] * 100000), 100000)
