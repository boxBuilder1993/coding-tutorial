from solution import closest_pairs
from checker import case

case("consecutive", closest_pairs([4, 2, 1, 3]), [[1, 2], [2, 3], [3, 4]])
case("one pair", closest_pairs([1, 3, 6, 10, 15]), [[1, 3]])
case("two items", closest_pairs([9, 2]), [[2, 9]])
case("negatives", closest_pairs([-5, 0, 5, 7]), [[5, 7]])
case("several equal gaps", closest_pairs([10, 1, 20, 11]), [[10, 11]])
