from solution import first_missing
from checker import case

case("three", first_missing([1, 2, 0]), 3)
case("two", first_missing([3, 4, -1, 1]), 2)
case("one", first_missing([7, 8, 9]), 1)
case("empty", first_missing([]), 1)
case("complete", first_missing([1, 2, 3]), 4)
case("duplicates", first_missing([1, 1, 2, 2]), 3)
case("large", first_missing(list(range(1, 100000)) + [100001]), 100000)
