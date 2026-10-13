import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    empty_lines_count = sum(1 for line in lines if not line.strip())
    
    valid_records = read_valid(lines)
    
    errors_count = len(lines) - empty_lines_count - len(valid_records)

    averages = average_by_city(valid_records)
    best_city = warmest_city(valid_records)
    
    if best_city:
        best_temp = averages[best_city]
    else:
        best_temp = 0.0
        
    print(len(valid_records))
    print(errors_count)
    print(f"{best_temp:.1f}")

if __name__ == "__main__":
    main()