from solution import is_priced
from checker import case
case("present", is_priced({"apple": 40}, "apple"), True)
case("absent", is_priced({"apple": 40}, "milk"), False)
case("value is not a key", is_priced({"apple": 40}, 40), False)
