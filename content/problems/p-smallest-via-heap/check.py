from solution import smallest
from checker import case
nums = [40, 25, 2.5]
case("three", smallest(nums), 2.5)
case("list unchanged", nums, [40, 25, 2.5])
case("one", smallest([7]), 7)
