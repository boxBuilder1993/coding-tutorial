from solution import no_vowels
from checker import case
case("sentence", no_vowels("sourdough bread"), "srdgh brd")
case("no vowels", no_vowels("xyz"), "xyz")
case("all vowels", no_vowels("aeiou"), "")
case("capitals kept", no_vowels("AEI"), "AEI")
