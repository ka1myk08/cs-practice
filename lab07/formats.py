import json


def csv_to_records(text: str) -> list[dict]:
    text = text.strip()
    if text == "":
        return []

    lines = text.split("\n")
    raw_headers = lines.split(",")
    headers = []
    for h in raw_headers:
        headers.append(h.strip())

    records = []

    for line in lines[1:]:
        if line.strip() == "":
            continue
        raw_values = line.split(",")
        row = {}
        for i in range(len(headers)):
            key = headers[i]
            val = raw_values[i].strip()
            row[key] = val
        records.append(row)

    return records


def convert_value(val: str):
    val = val.strip()
    low = val.lower()

    if low == "true" or low == "yes":
        return True
    if low == "false" or low == "no":
        return False


    try:
        return int(val)
    except ValueError:
        pass


    try:
        return float(val)
    except ValueError:
        pass


    return val


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_name = ""

    for line in lines:
        if "#" in line:
            parts = line.split("#")
            line = parts


        if line.strip() == "":
            continue

        clean_line = line.strip()


        if clean_line.startswith("- "):
            item = clean_line[2:]  # убираем "- " в начале
            result[current_list_name].append(convert_value(item))
        else:
            parts = clean_line.split(":", 1)
            key = parts.strip()
            val = parts[1].strip()

            if val == "":
                result[key] = []
                current_list_name = key
            else:
                result[key] = convert_value(val)
                current_list_name = ""

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    answer = []

    for row in rows:
        new_row = {}
        id_value = row.get(key)

        if id_value in extra:
            info_from_extra = extra[id_value]
            for k in info_from_extra:
                new_row[k] = info_from_extra[k]

        for k in row:
            new_row[k] = row[k]

        answer.append(new_row)

    return answer


def records_to_json(records: list[dict]) -> str:


    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)