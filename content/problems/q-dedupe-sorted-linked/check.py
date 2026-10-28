from solution import dedupe
from checker import case, from_list, to_list

case("classic", to_list(dedupe(from_list([1, 1, 2, 3, 3]))), [1, 2, 3])
case("empty", dedupe(None), None)
case("no duplicates", to_list(dedupe(from_list([1, 2]))), [1, 2])
case("all same", to_list(dedupe(from_list([4, 4, 4]))), [4])
case("triples", to_list(dedupe(from_list([1, 1, 1, 2, 2, 3]))), [1, 2, 3])
