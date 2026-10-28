from solution import nearby_duplicate
from checker import case

case("just within", nearby_duplicate([1, 2, 3, 1], 3), True)
case("too far", nearby_duplicate([1, 2, 3, 1, 2, 3], 2), False)
case("adjacent", nearby_duplicate([1, 0, 1, 1], 1), True)
case("no duplicates", nearby_duplicate([1, 2, 3], 10), False)
case("empty", nearby_duplicate([], 1), False)
case("k zero never", nearby_duplicate([1, 1], 0), False)
