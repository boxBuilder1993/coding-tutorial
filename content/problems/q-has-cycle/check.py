from solution import has_cycle
from checker import case, from_list

head = from_list([1, 2, 3, 4])
head.next.next.next.next = head.next
case("cycle to second node", has_cycle(head), True)
case("no cycle", has_cycle(from_list([1, 2, 3])), False)
case("empty", has_cycle(None), False)
single = from_list([1])
case("single, no cycle", has_cycle(single), False)
single.next = single
case("single pointing at itself", has_cycle(single), True)
two = from_list([1, 2])
two.next.next = two
case("two-node loop", has_cycle(two), True)
