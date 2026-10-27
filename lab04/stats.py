def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("нужно ровно три поля")
    
    city = parts[0].strip()
    temperature = parts[1].strip()
    date = parts[2].strip()
    
    if city == "":
        raise ValueError("город пустой")
    
    if date == "":
        raise ValueError("дата пустая")
    
    try:
        temp = float(temperature)
    except ValueError:
        raise ValueError("температура не является числом")
    
    return {"city": city, "temp": temp, "date": date}

      
def read_valid(lines: list[str]) -> list[dict]:
    result = []
    for line in lines:
        if line.strip() == "":
            continue
        try:
            record = parse_record(line)
            result.append(record)
        except ValueError:
            pass
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
        averages[city] = round(total[city] / count[city], 1)
    return averages


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    best = ""
    for city in averages:
        if best == "":
            best = city
        elif averages[city] > averages[best]:
            best = city
        elif averages[city] == averages[best] and city < best:
            best = city
    return best

