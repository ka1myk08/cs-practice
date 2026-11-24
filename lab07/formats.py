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


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_name = ""

    for line in lines:
        if "#" in line:
            line, _comment = line.split("#", 1)

        clean_line = line.strip()
        if clean_line == "":
            continue

        is_list_item = False
        key = ""
        raw_val = ""

        if clean_line.startswith("-"):
            if current_list_name == "":
                continue
            is_list_item = True
            raw_val = clean_line[1:].strip()
        elif ":" in clean_line:
            key, val = clean_line.split(":", 1)
            key = key.strip()
            raw_val = val.strip()

            if raw_val == "":
                result[key] = []
                current_list_name = key
                continue
            else:
                current_list_name = ""
        else:
            continue

        low = raw_val.lower()
        num_check = raw_val
        if num_check.startswith("-") or num_check.startswith("+"):
            num_check = num_check[1:]

        if low == "true" or low == "yes":
            converted = True
        elif low == "false" or low == "no":
            converted = False
        elif num_check.isdigit():
            converted = int(raw_val)
        elif num_check.count(".") == 1:
            left, right = num_check.split(".")
            if left.isdigit() and right.isdigit():
                converted = float(raw_val)
            else:
                converted = raw_val
        else:
            converted = raw_val

        if is_list_item:
            result[current_list_name].append(converted)
        else:
            result[key] = converted

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



