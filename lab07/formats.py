import json


def csv_to_records(text: str) -> list[dict]:
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    if len(lines) < 2:
        return []

    header_line, *data_lines = lines
    headers = [h.strip() for h in header_line.split(",")]
    records = []

    for line in data_lines:
        values = [v.strip() for v in line.split(",")]
        row = {}
        for i in range(len(headers)):
            row[headers[i]] = values[i] if i < len(values) else ""
        records.append(row)

    return records


def parse_settings(lines: list[str]) -> dict:
    def parse_value(raw: str):
        val = raw.strip()
        if val in ("true", "yes"):
            return True
        if val in ("false", "no"):
            return False

        unsigned = val[1:] if val.startswith(("-", "+")) else val
        if unsigned.isdigit():
            return int(val)
        if unsigned.count(".") == 1:
            left, right = unsigned.split(".")
            if left.isdigit() and right.isdigit():
                return float(val)

        return val

    result = {}
    current_list = None

    for line in lines:
        if "#" in line:
            line, _ = line.split("#", 1)
        clean = line.strip()
        if not clean:
            continue

        if clean.startswith("- "):
            if current_list is not None:
                result[current_list].append(parse_value(clean[2:]))
        elif clean == "-":
            if current_list is not None:
                result[current_list].append("")
        elif ":" in clean:
            key, val = clean.split(":", 1)
            key = key.strip()
            val = val.strip()
            if val == "":
                result[key] = []
                current_list = key
            else:
                result[key] = parse_value(val)
                current_list = None

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        merged = {}
        key_val = row.get(key)
        if key_val in extra:
            merged.update(extra[key_val])
        merged.update(row)
        result.append(merged)
    return result


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)




