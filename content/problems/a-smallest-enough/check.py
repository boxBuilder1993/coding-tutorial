from solution import smallest_capacity
from checker import case

case("two boxes", smallest_capacity([1, 2, 3, 4, 5], 2), 9)
case("one item per box", smallest_capacity([1, 2, 3, 4, 5], 5), 5)
case("classic", smallest_capacity([7, 2, 5, 10, 8], 2), 18)
case("one box takes everything", smallest_capacity([3, 3, 3], 1), 9)
case("more boxes than items", smallest_capacity([4, 9], 5), 9)
case("single item", smallest_capacity([6], 1), 6)
case("larger", smallest_capacity(list(range(1, 101)), 10), 540)
