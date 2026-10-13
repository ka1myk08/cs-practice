# Шаг 4: Финальная версия. Расчет средних температур и поиск теплого города
def parse_record(line: str) -> dict:
    parts = line.split(";")
    
    if len(parts) != 3:
        raise ValueError("Ошибка: не 3 поля")
        
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    if city == "" or date == "":
        raise ValueError("Ошибка: пустое поле")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Ошибка: температура не число")
    return {"city": city, "temp": temp, "date": date}


def read_valid(lines: list) -> tuple:
    valid_records = []
    errors_count = 0
    
    for line in lines:
        cleaned = line.strip()

        if cleaned == "":
            continue
            
        try:
            record = parse_record(cleaned)
            valid_records.append(record)
        except ValueError:
            errors_count += 1
            
    return valid_records, errors_count


def average_by_city(records: list) -> dict:
    city_temps = {}

    for rec in records:
        city = rec["city"]
        temp = rec["temp"]
        
        if city not in city_temps:
            city_temps[city] = []
        city_temps[city].append(temp)
    averages = {}
    for city in city_temps:
        temps_list = city_temps[city]
        avg = sum(temps_list) / len(temps_list)
        averages[city] = round(avg, 1)
        
    return averages


def warmest_city(records: list) -> str:
    if not records:
        return ""
        
    averages = average_by_city(records)
    
    best_city = ""
    max_temp = -999.0
    
    for city in averages:
        current_temp = averages[city]
        
        if current_temp > max_temp:
            max_temp = current_temp
            best_city = city
        elif current_temp == max_temp:
            if best_city == "" or city < best_city:
                best_city = city
                
    return best_city