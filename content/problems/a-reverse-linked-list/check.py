from solution import reverse
from checker import case, from_list, to_list

case("four nodes", to_list(reverse(from_list([1, 2, 3, 4]))), [4, 3, 2, 1])
case("empty", reverse(None), None)
case("single", to_list(reverse(from_list([7]))), [7])
case("two", to_list(reverse(from_list(["a", "b"]))), ["b", "a"])
head = from_list([1, 2, 3])
first = head
new_head = reverse(head)
case("reuses the original nodes", first.next is None and to_list(new_head) == [3, 2, 1], True)
