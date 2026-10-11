from solution import valid_codes
from checker import case
case("mixed", valid_codes(["BRD-001", "brd-001", "BRD-01", "MLK-010", "BRD001"]), ["BRD-001", "MLK-010"])
case("empty", valid_codes([]), [])
case("digits where letters should be", valid_codes(["123-456"]), [])
case("letters where digits should be", valid_codes(["ABC-DEF"]), [])
case("too long", valid_codes(["ABCD-001"]), [])
