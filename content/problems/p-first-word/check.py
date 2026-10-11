from solution import first_word
from checker import case
case("three words", first_word("fresh bread daily"), "fresh")
case("one word", first_word("milk"), "milk")
case("leading spaces", first_word("   apple pie"), "apple")
