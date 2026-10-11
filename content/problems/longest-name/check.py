from solution import longest
from checker import case

case("clear winner", longest(["apple", "bread", "sourdough"]), "sourdough")
case("tie keeps the first", longest(["milk", "eggs"]), "milk")
case("single", longest(["flour"]), "flour")
case("longest at the start", longest(["sourdough", "milk", "eggs"]), "sourdough")
