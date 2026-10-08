from solution import batch
from checker import case

case("long code", batch("SKU-1042-A7B"), "A7B")
case("short code", batch("BRD-001"), "001")
case("exactly three characters", batch("XYZ"), "XYZ")
case("digits", batch("1234567"), "567")
