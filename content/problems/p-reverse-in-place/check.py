from solution import reverse_in_place
from checker import case
case("even length", reverse_in_place([1, 2, 3, 4]), [4, 3, 2, 1])
case("odd length", reverse_in_place([1, 2, 3]), [3, 2, 1])
case("empty", reverse_in_place([]), [])
case("single", reverse_in_place([1]), [1])
items = [1, 2]
result = reverse_in_place(items)
case("same list object", result is items, True)
