from solution import normalise
from checker import case

case("spaces and capitals", normalise("  Sourdough Bread "), "sourdough bread")
case("all capitals", normalise("MILK"), "milk")
case("already clean", normalise("apple"), "apple")
case("inner spaces are kept", normalise(" a  b "), "a  b")
