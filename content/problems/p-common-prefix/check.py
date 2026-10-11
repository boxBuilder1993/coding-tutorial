from solution import common_prefix
from checker import case
case("partial", common_prefix("sourdough", "soup"), "sou")
case("nothing", common_prefix("milk", "bread"), "")
case("one is a prefix of the other", common_prefix("bread", "breadcrumbs"), "bread")
case("empty", common_prefix("", "x"), "")
case("identical", common_prefix("milk", "milk"), "milk")
case("stops at the first difference", common_prefix("abxd", "abyd"), "ab")
