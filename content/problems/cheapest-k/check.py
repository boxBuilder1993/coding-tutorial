from solution import cheapest
from checker import case

case("two cheapest", cheapest([40, 25, 2.5, 60, 15], 2), [2.5, 15])
case("k larger than list", cheapest([40, 25], 5), [25, 40])
case("k is zero", cheapest([1, 2, 3], 0), [])
case("duplicates", cheapest([5, 1, 1, 3], 3), [1, 1, 3])
original = [3, 1, 2]
cheapest(original, 1)
case("original is unchanged", original, [3, 1, 2])
