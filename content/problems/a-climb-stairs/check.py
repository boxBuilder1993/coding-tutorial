from solution import ways
from checker import case

case("zero steps", ways(0), 1)
case("one step", ways(1), 1)
case("two steps", ways(2), 2)
case("three steps", ways(3), 3)
case("four steps", ways(4), 5)
case("ten steps", ways(10), 89)
case("forty steps", ways(40), 165580141)
