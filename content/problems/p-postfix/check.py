from solution import evaluate
from checker import case
case("add", evaluate("3 4 +"), 7)
case("nested", evaluate("3 4 + 2 *"), 14)
case("subtraction order", evaluate("10 2 3 * -"), 4)
case("single number", evaluate("42"), 42)
case("negative result", evaluate("2 5 -"), -3)
case("chain", evaluate("1 2 3 4 + + +"), 10)
