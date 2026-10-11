from solution import dedupe
from checker import case
nums = [1, 1, 2, 3, 3, 3]
n = dedupe(nums)
case("count of unique values", n, 3)
case("prefix holds the unique values in order", nums[:3], [1, 2, 3])
case("empty", dedupe([]), 0)
case("single", dedupe([7]), 1)
alldup = [2, 2, 2]
case("all duplicates count", dedupe(alldup), 1)
case("all duplicates prefix", alldup[:1], [2])
distinct = [1, 2, 3]
case("already unique", dedupe(distinct), 3)
case("already unique list unchanged", distinct, [1, 2, 3])
