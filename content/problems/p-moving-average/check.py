from solution import moving_averages
from checker import case
case("window of two", moving_averages([10, 20, 30, 40], 2), [10.0, 15.0, 25.0, 35.0])
case("window larger than data", moving_averages([3, 6, 9], 5), [3.0, 4.5, 6.0])
case("empty", moving_averages([], 3), [])
case("rounding", moving_averages([1, 2, 2], 3), [1.0, 1.5, 1.67])
