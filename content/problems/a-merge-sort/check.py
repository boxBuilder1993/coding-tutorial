from solution import merge_sort
from checker import case
import random

case("mixed", merge_sort([8, 3, 12, 5, 1, 9, 3]), [1, 3, 3, 5, 8, 9, 12])
case("empty", merge_sort([]), [])
case("single", merge_sort([4]), [4])
case("already sorted", merge_sort([1, 2, 3]), [1, 2, 3])
case("reverse sorted", merge_sort([3, 2, 1]), [1, 2, 3])
case("strings", merge_sort(["milk", "apple", "bread"]), ["apple", "bread", "milk"])
original = [3, 1, 2]
merge_sort(original)
case("does not change the input", original, [3, 1, 2])
rng = random.Random(7)
big = [rng.randint(0, 10 ** 6) for _ in range(50000)]
case("fifty thousand items", merge_sort(big), sorted(big))
