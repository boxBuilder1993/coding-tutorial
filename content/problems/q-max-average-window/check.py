from solution import max_average
from checker import case

case("classic", max_average([1, 12, -5, -6, 50, 3], 4), 12.75, compare="approx")
case("single", max_average([5], 1), 5.0, compare="approx")
case("whole list", max_average([1, 2, 3], 3), 2.0, compare="approx")
case("negatives", max_average([-1, -2, -3], 2), -1.5, compare="approx")
big = [(i * 7) % 13 for i in range(100000)]
prefix = [0]
for x in big:
    prefix.append(prefix[-1] + x)
expected = max(prefix[i + 50000] - prefix[i] for i in range(len(big) - 50000 + 1)) / 50000
case("a hundred thousand", max_average(big, 50000), expected, compare="approx")
