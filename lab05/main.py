import os

from logstats import count_levels, format_report, top_errors

name = input().strip()

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, name)

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)

with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

total = 0
for level in counts:
    total += counts[level]

print(total)
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

report_path = os.path.join(folder, "report.txt")
with open(report_path, "w", encoding="utf-8", newline="\n") as out:
    out.write(format_report(counts, errors))
    