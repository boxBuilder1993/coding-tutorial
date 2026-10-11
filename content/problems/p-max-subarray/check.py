from solution import best_run
from checker import case
case("example", best_run([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
case("all negative", best_run([-3, -1, -2]), -1)
case("all positive", best_run([1, 2, 3]), 6)
case("single", best_run([-7]), -7)
case("best at the end", best_run([-1, -1, 5, 5]), 10)
