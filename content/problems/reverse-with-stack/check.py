from solution import reverse_items
from checker import case

case("three items", reverse_items(["apple", "bread", "milk"]), ["milk", "bread", "apple"])
case("empty", reverse_items([]), [])
case("single", reverse_items([1]), [1])
original = [1, 2, 3]
reverse_items(original)
case("original is unchanged", original, [1, 2, 3])
