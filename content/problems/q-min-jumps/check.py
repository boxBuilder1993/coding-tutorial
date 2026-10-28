from solution import min_jumps
from checker import case

case("classic", min_jumps([2, 3, 1, 1, 4]), 2)
case("ones", min_jumps([1, 1, 1]), 2)
case("already there", min_jumps([5]), 0)
case("one big jump", min_jumps([4, 1, 1, 1, 1]), 1)
case("two items", min_jumps([1, 9]), 1)
case("long", min_jumps([2] * 1001), 500)
