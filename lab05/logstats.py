def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("нужно три части")

    time = parts[0]
    level = parts[1]
    message = parts[2]

    if level != "DEBUG" and level != "INFO" and level != "WARNING" and level != "ERROR":
        raise ValueError("неизвестный уровень")

    return {"time": time, "level": level, "message": message}

