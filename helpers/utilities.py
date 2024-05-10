import msvcrt


def counter_apples(
        field: list[list[str]]
) -> int:
    """
    Подсчет количества яблочек на текущем поле
    :param field: Двумерный массив c данными о текущем поле
    :return: количество яблочек
    """
    count = 0
    for row in field:
        count_in_row = row.count('*')
        count += count_in_row
    return count


def get_key():
    """
    На вход ничего не передается
    Считывание нажатия клавиши
    :return: нажатая клавиша
    """
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            return key