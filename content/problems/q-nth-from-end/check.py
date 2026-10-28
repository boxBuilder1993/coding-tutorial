from solution import nth_from_end
from checker import case, from_list

case("second from end", nth_from_end(from_list([1, 2, 3, 4, 5]), 2), 4)
case("first node", nth_from_end(from_list([1, 2, 3, 4, 5]), 5), 1)
case("last node", nth_from_end(from_list([1, 2, 3, 4, 5]), 1), 5)
case("single", nth_from_end(from_list([9]), 1), 9)
