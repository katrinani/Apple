def go_up(
        field: list[list[str]],
        position: list,
        data: list
):
    """
    Функция, определяющая по нынешнему положению пользователя,
    возможно ли пойти вверх и передвигает его, если возможно
    :param field: текущее поле
    :param position: ныняшняя позиция пользователя
    :param data: текущий счет и количество оставшихся яблок
    """
    if position[0] - 1 >= 0:
        if field[position[0] - 1][position[1]] == '*':
            data[0] += 1
            data[1] -= 1
        field[position[0]][position[1]] = ' '
        field[position[0] - 1][position[1]] = '☺'
        position[0] -= 1
    else:
        print('Вы не можете идти туда!')


def go_down(
        field: list[list[str]],
        position: list,
        data: list,
        len_row: int
):
    """
    Функция, определяющая по нынешнему положению пользователя,
    возможно ли пойти вниз и передвигает его, если возможно
    :param field: текущее поле
    :param position: ныняшняя позиция пользователя
    :param data: текущий счет и количество оставшихся яблок
    :param len_row: количество строк
    """
    if position[0] + 1 < len_row:
        if field[position[0] + 1][position[1]] == '*':
            data[0] += 1
            data[1] -= 1
        field[position[0]][position[1]] = ' '
        field[position[0] + 1][position[1]] = '☺'
        position[0] += 1
    else:
        print('Вы не можете идти туда!')


def go_right(
        field: list[list[str]],
        position: list,
        data: list,
        len_column: int
):
    """
    Функция, определяющая по нынешнему положению пользователя,
    возможно ли пойти вправо и передвигает его, если возможно
    :param field: текущее поле
    :param position: ныняшняя позиция пользователя
    :param data: текущий счет и количество оставшихся яблок
    :param len_column: колиечство столбцов
    """
    if position[1] + 1 < len_column:
        if field[position[0]][position[1] + 1] == '*':
            data[0] += 1
            data[1] -= 1
        field[position[0]][position[1]] = ' '
        field[position[0]][position[1] + 1] = '☺'
        position[1] += 1
    else:
        print('Вы не можете идти туда!')


def go_left(
        field: list[list[str]],
        position: list,
        data: list
):
    """
    Функция, определяющая по нынешнему положению пользователя,
    возможно ли пойти влево и передвигает его, если возможно
    :param field: текущее поле
    :param position: ныняшняя позиция пользователя
    :param data: текущий счет и количество оставшихся яблок
    """
    if position[1] - 1 >= 0:
        if field[position[0]][position[1] - 1] == '*':
            data[0] += 1
            data[1] -= 1
        field[position[0]][position[1]] = ' '
        field[position[0]][position[1] - 1] = '☺'
        position[1] -= 1
    else:
        print('Вы не можете идти туда!')
