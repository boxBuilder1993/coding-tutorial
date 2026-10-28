from solution import case_variants
from checker import case

case("a1b", case_variants("a1b"), ["a1b", "a1B", "A1b", "A1B"], compare="sorted")
case("digits only", case_variants("12"), ["12"], compare="sorted")
case("empty", case_variants(""), [""], compare="sorted")
case("one letter", case_variants("C"), ["c", "C"], compare="sorted")
case("count", len(case_variants("ab3cd")), 16)
