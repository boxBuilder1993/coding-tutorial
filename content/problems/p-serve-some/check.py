from solution import remaining
from checker import case
case("serve two", remaining(["Ada", "Grace", "Linus"], 2), ["Linus"])
case("serve more than there are", remaining(["Ada"], 5), [])
case("serve none", remaining(["Ada"], 0), ["Ada"])
case("returns a list", type(remaining(["a"], 0)).__name__, "list")
