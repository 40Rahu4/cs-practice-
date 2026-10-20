def read_rows(lines: list[str]) -> list[dict]:
    headers = None
    rows = []

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        fields = line.split(",")

        for i in range(len(fields)):
            fields[i] = fields[i].strip()

        if headers is None:
            headers = fields
        elif len(fields) == len(headers):
            row = {}

            for i in range(len(headers)):
                row[headers[i]] = fields[i]

            rows.append(row)

    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}

    for row in rows:
        kind = row["тип"]

        if kind in counts:
            counts[kind] += 1
        else:
            counts[kind] = 1

    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0

    for row in rows:
        if row["тип"] == kind:
            value = row["минуты"].replace(",", ".")

            try:
                total += float(value)
            except ValueError:
                pass

    return round(total, 1)


def to_csv(counts: dict) -> str:
    result = "тип,количество\n"

    for kind in sorted(counts):
        result += kind + "," + str(counts[kind]) + "\n"

    return result