import random
from data.borders import (
    top_right,
    top_left,
    bottom_left,
    bottom_right,
    horizontal,
    vertical
)


def field_generation(
        row: int,
        column: int
) -> list[list[str]]:
    """
    Функция, генерирующая поле для игры
    :param row: количество строк
    :param column: количество столбцов
    :return: двумерный массив, в котором находятся обьекты и путые строки
    """
    element_field = ['*', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*']
    field = []

    for _ in range(row):
        current_row = []
        for _ in range(column):
            current_row.append(random.choice(element_field))
        field.append(current_row)

    field[0][0] = '☺'  # пользователь начинает с верхнего левого угла

    return field


def field_output(
        len_column: int,
        score: int,
        field: list[list[str]]
):
    """
    Функция, выводящая поле, обрамленное рамкой из двойных линий
    :param len_column: количество столбцов
    :param score: текущий счет
    :param field: текущее поле
    """
    print(f'Score: {score}')
    print(top_left + horizontal * (len_column + 4) + top_right)
    for row in field:
        print(vertical + '  ', end='')
        for j in range(len(row)):
            print(row[j], end='')
        print('  ' + vertical)
    print(bottom_left + horizontal * (len_column + 4) + bottom_right)
