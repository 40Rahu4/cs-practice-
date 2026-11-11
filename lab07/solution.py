import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []

    array = np.asarray(values, dtype=float)
    rows = array.reshape(-1, width)
    return rows.tolist()


def block(
    matrix: list[list[float]],
    rows: list[int],
    columns: list[int],
) -> list[list[float]]:
    if not matrix or not rows or not columns:
        return []

    array = np.asarray(matrix, dtype=float)
    selected = array[np.ix_(rows, columns)]
    return selected.tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []

    array = np.asarray(matrix, dtype=float)
    means = np.round(array.mean(axis=0), 6)
    return means.tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0

    array = np.asarray(matrix, dtype=float)
    values = array[:, column]
    return float(np.round(values.max() - values.min(), 6))