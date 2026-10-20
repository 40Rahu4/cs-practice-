from tablestats import read_rows, count_types, total_minutes, to_csv


filename = input()

with open(filename, encoding="utf-8") as table:
    rows = read_rows(table)

counts = count_types(rows)

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(str(len(rows)) + '\n')
    out.write(str(len(counts)) + '\n')
    out.write(str(total_minutes(rows, "ошибка")) + '\n')