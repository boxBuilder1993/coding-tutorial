from solution import has_space
from checker import case

case("two words", has_space("sourdough bread"), True)
case("one word", has_space("bread"), False)
case("empty string", has_space(""), False)
case("only a space", has_space(" "), True)
case("space at the end", has_space("bread "), True)
