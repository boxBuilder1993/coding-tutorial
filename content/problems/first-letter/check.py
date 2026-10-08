from solution import first_letter
from checker import case

case("lowercase word", first_letter("bread"), "B")
case("already capital", first_letter("Milk"), "M")
case("single character", first_letter("x"), "X")
case("two words", first_letter("sourdough bread"), "S")
