from solution import selection_sort
from checker import case
case("example", selection_sort([5, 1, 4, 2]), [1, 2, 4, 5])
case("empty", selection_sort([]), [])
case("single", selection_sort([1]), [1])
case("reversed", selection_sort([3, 2, 1]), [1, 2, 3])
case("duplicates", selection_sort([2, 1, 2, 1]), [1, 1, 2, 2])
nums = [9, 8, 7]
selection_sort(nums)
case("sorts in place", nums, [7, 8, 9])
