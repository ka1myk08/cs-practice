def parse_record(line: str) -> dict:
    city, temp, date = line.spli(";")
    return {"city": city, "temperature": float(temp), "date": date}

      
def read_valid(lines: list[str]) -> list[dict]:
    result = []
    for line in lines:
        result.append(parse_record(line))
    return result
    
    
def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        if city not in total:
            total[city] = 0
            count[city] = 0
        total[city] += rec["temp"]
        count[city] += 1

    averages = {}
    for city in total:
        averages[city] = total[city] / count[city]
    return averages


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    best = ""
    for city in averages:
        if best == "" or averages[city] > averages[best]:
            best = city
    return best
