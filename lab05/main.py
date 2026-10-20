from tablestats import read_rows, count_types, total_minutes, to_csv


filename = input()

with open(filename, encoding="utf-8") as table:
    rows = read_rows(table)

counts = count_types(rows)

with open("summary.csv", "w", encoding="utf-8") as out:
    print(len(rows), file=out)
    print(len(counts), file=out)
    print(total_minutes(rows, "ошибка"), file=out)