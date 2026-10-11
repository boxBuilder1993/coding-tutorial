from solution import longest_word
from checker import case
case("clear winner", longest_word("fresh sourdough bread"), "sourdough")
case("tie keeps first", longest_word("milk eggs"), "milk")
case("one word", longest_word("apple"), "apple")
