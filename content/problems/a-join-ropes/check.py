from solution import join_cost
from checker import case

case("four ropes", join_cost([4, 3, 2, 6]), 29)
case("single rope", join_cost([5]), 0)
case("two ropes", join_cost([1, 2]), 3)
case("equal ropes", join_cost([1, 1, 1, 1]), 8)
case("already sorted descending", join_cost([10, 5, 1]), 22)
original = [4, 3]
join_cost(original)
case("may or may not change the input, but gives the right answer", join_cost([4, 3]), 7)
