import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()

records = read_valid(lines)
best = warmest_city(records)
averages = average_by_city(records)

print(len(records))
print(0)
print(averages[best])
