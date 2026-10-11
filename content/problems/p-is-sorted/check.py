from solution import is_ascending
from checker import case
case("ascending with repeat", is_ascending([1, 2, 2, 5]), True)
case("descending", is_ascending([3, 1]), False)
case("empty", is_ascending([]), True)
case("single", is_ascending([7]), True)
case("dip in the middle", is_ascending([1, 5, 3, 9]), False)
