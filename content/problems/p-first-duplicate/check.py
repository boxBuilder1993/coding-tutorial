from solution import first_duplicate
from checker import case
case("milk repeats first", first_duplicate(["milk", "bread", "milk", "bread"]), "milk")
case("none", first_duplicate([1, 2, 3]), None)
case("empty", first_duplicate([]), None)
case("second appearance decides", first_duplicate([1, 2, 2, 1]), 2)
