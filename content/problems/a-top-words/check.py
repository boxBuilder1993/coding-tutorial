from solution import top_words
from checker import case

case("clear leaders", top_words("the cat sat on the mat the cat ran", 2), ["the", "cat"])
case("ties alphabetical", top_words("b a b a c", 3), ["a", "b", "c"])
case("k is 1", top_words("x y y", 1), ["y"])
case("all words", top_words("one two two three three three", 3), ["three", "two", "one"])
case("tie between the top two", top_words("pear apple pear apple fig", 1), ["apple"])
