from solution import first_true
from checker import case

case("mixed", first_true([False, False, True, True]), 2)
case("all true", first_true([True]), 0)
case("all false", first_true([False, False]), 2)
case("empty", first_true([]), 0)
case("last only", first_true([False, False, False, True]), 3)
big = [False] * 777777 + [True] * 222223
case("a million flags", first_true(big), 777777)
