def winner(names: list[str], scores: list[float]) -> str:
    best_index = 0

    for i in range(1, len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i

    return names[best_index]

def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return 0.0

    total = 0

    for score in scores:
        total += score

    return (total / len(scores))

def ranking(names: list[str], scores: list[float]) -> list[str]:
    ind = list(range(len(names)))

    ind.sort(key=lambda i: scores[i], reverse=True)

    result = []

    for i in ind:
        result.append(names[i])

    return result

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    result = []

    for i in range(len(names)):
        if scores[i] > avg:
            result.append(names[i])

    return result
names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
print(winner(names , scores))
print(average(scores))
print(ranking(names , scores))
print(above_average(names , scores))