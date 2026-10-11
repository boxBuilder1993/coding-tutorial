from solution import merge_slots
from checker import case
case("example", merge_slots([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
case("touching", merge_slots([[1, 4], [4, 5]]), [[1, 5]])
case("unsorted input", merge_slots([[5, 7], [1, 3], [2, 4]]), [[1, 4], [5, 7]])
case("contained", merge_slots([[1, 10], [2, 3]]), [[1, 10]])
case("empty", merge_slots([]), [])
data = [[5, 7], [1, 3], [2, 4]]
merge_slots(data)
case("input unchanged", data, [[5, 7], [1, 3], [2, 4]])
