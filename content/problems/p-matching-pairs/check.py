from solution import pairs_summing
from checker import case
case("two pairs", pairs_summing([10, 30, 20, 30], 40), 2)
case("single element", pairs_summing([5], 10), 0)
case("no pairs", pairs_summing([1, 2, 3], 100), 0)
case("same value twice", pairs_summing([20, 20], 40), 1)
case("does not pair an element with itself", pairs_summing([20], 40), 0)
