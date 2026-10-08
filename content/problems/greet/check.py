from solution import greet
from checker import case

case("Ada", greet("Ada"), "Hello, Ada!")
case("empty name", greet(""), "Hello, !")
case("name with space", greet("Grace Hopper"), "Hello, Grace Hopper!")
