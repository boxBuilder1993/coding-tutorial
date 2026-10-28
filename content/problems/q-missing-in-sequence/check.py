from solution import missing
from checker import case

case("middle", missing([0, 1, 2, 4, 5]), 3)
case("zero missing", missing([1, 2, 3]), 0)
case("last missing", missing([0, 1, 2]), 3)
case("empty, so zero", missing([]), 0)
case("one item", missing([0]), 1)
big = [i for i in range(10 ** 6) if i != 424242]
case("a million items", missing(big), 424242)
