from solution import is_bakery
from checker import case

case("bakery code", is_bakery("BRD-001"), True)
case("other department", is_bakery("MLK-010"), False)
case("prefix in the middle does not count", is_bakery("X-BRD-001"), False)
case("prefix only", is_bakery("BRD-"), True)
case("lowercase does not match", is_bakery("brd-001"), False)
