from solution import insertion_sort
from checker import case
case("example", insertion_sort([5, 1, 4, 2]), [1, 2, 4, 5])
case("empty", insertion_sort([]), [])
case("single", insertion_sort([1]), [1])
case("reversed", insertion_sort([3, 2, 1]), [1, 2, 3])
case("duplicates", insertion_sort([2, 1, 2, 1]), [1, 1, 2, 2])
case("insert at the front", insertion_sort([2, 3, 1]), [1, 2, 3])
nums = [9, 8, 7]
insertion_sort(nums)
case("sorts in place", nums, [7, 8, 9])
