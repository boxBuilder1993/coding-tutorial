from solution import initials
from checker import case
case("two words", initials("ada lovelace"), "AL")
case("three words", initials("grace brewster hopper"), "GBH")
case("one word", initials("linus"), "L")
case("already capitals", initials("Ada Lovelace"), "AL")
