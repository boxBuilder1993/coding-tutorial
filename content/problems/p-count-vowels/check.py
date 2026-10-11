from solution import vowels
from checker import case
case("sourdough", vowels("sourdough"), 4)
case("none", vowels("xyz"), 0)
case("empty", vowels(""), 0)
case("capitals do not count", vowels("AEIOU"), 0)
