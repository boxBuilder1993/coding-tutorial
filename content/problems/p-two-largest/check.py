from solution import top_two
from checker import case
case("four", top_two([40, 25, 2.5, 60]), [60, 40])
case("two", top_two([1, 2]), [2, 1])
case("duplicates", top_two([5, 5, 1]), [5, 5])
