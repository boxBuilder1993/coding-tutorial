from solution import closest_pair_sum
from checker import case

case("tie goes to smaller", closest_pair_sum([1, 3, 5, 8, 12], 10), 9)
case("exact match", closest_pair_sum([1, 3, 5, 8, 12], 20), 20)
case("negatives", closest_pair_sum([-4, -1, 2, 6], 0), 1)
case("two items only", closest_pair_sum([2, 9], 100), 11)
case("target below everything", closest_pair_sum([5, 6, 7], 0), 11)
case("repeats", closest_pair_sum([1, 1, 1, 10], 2), 2)
big = list(range(0, 200000, 2))
case("a hundred thousand items", closest_pair_sum(big, 123457), 123456)
