from solution import fib
from checker import case

case("fib(0)", fib(0), 0)
case("fib(1)", fib(1), 1)
case("fib(10)", fib(10), 55)
case("fib(30)", fib(30), 832040)
case("fib(90)", fib(90), 2880067194370816120)
a, b = 0, 1
for _ in range(3000):
    a, b = b, a + b
case("fib(3000)", fib(3000), a)
