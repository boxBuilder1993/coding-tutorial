from solution import most_meetings
from checker import case

case("classic set", most_meetings([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]), 3)
case("empty", most_meetings([]), 0)
case("one long one blocks shorter ones", most_meetings([(1, 10), (2, 3), (4, 5)]), 2)
case("touching ends are fine", most_meetings([(1, 2), (2, 3), (3, 4)]), 3)
case("all overlap", most_meetings([(1, 5), (2, 6), (3, 7)]), 1)
case("unsorted input", most_meetings([(5, 6), (1, 2), (3, 4)]), 3)
