# Шаг 4: Финальная версия. Расчет средних температур и поиск теплого города
def parse_record(line: str) -> dict:

    parts = line.split(";")
    
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля")
        
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    if not city or not date:
        raise ValueError("Город или дата не могут быть пустыми")
        
    temperature = float(temp_str)
        
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:

    valid_records = []
    
    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue
            
        try:
            record = parse_record(cleaned)
            valid_records.append(record)
        except ValueError:
            pass
            
    return valid_records


def average_by_city(records: list[dict]) -> dict:

    city_temps = {}
    
    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]
        
        if city not in city_temps:
            city_temps[city] = []
        city_temps[city].append(temp)
        
    averages = {}
    for city, temps in city_temps.items():
        averages[city] = round(sum(temps) / len(temps), 1)
        
    return averages


def warmest_city(records: list[dict]) -> str:

    if not records:
        return ""
        
    averages = average_by_city(records)
    
    best_city = ""
    max_temp = float("-inf")
    
    for city in sorted(averages.keys()):
        current_temp = averages[city]
        if current_temp > max_temp:
            max_temp = current_temp
            best_city = city
            
    return best_city