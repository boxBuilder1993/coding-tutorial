from solution import can_serve_all
from checker import case

case("works", can_serve_all([5, 5, 5, 10, 20]), True)
case("fails", can_serve_all([5, 5, 10, 10, 20]), False)
case("first customer has a ten", can_serve_all([10]), False)
case("empty", can_serve_all([]), True)
case("prefer the ten when breaking a twenty", can_serve_all([5, 5, 5, 10, 20, 5, 20]), False)
case("three fives for a twenty", can_serve_all([5, 5, 5, 20]), True)
