from solution import spellings
from checker import case

case("23", spellings("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], compare="sorted")
case("empty", spellings(""), [])
case("single key", spellings("7"), ["p", "q", "r", "s"], compare="sorted")
case("count 79", len(spellings("79")), 16)
case("count 2345", len(spellings("2345")), 81)
