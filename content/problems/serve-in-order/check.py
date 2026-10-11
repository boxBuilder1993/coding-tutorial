from solution import serve_all
from checker import case

case("three customers", serve_all(["Ada", "Grace", "Linus"]), ["Ada", "Grace", "Linus"])
case("empty", serve_all([]), [])
case("one", serve_all(["Ada"]), ["Ada"])
original = ["a", "b"]
serve_all(original)
case("input list is unchanged", original, ["a", "b"])
