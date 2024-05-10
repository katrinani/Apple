"""
Задача ИГРА "Яблочки":
1. Необходимо нарисовать игровое поле N на M. (подсказка положение игрока и яблоки хранятся в двумерном массиве).
Ограничить поле двойными полосами.
2. Найти специальные символы смайлик (для игрока) и яблоко (для яблок) (используйте функции ord и chr)
3. В произвольном порядке расставить яблоки
4. Игрок может перемещаться по игровому полю по нажатию клавиши (вверх, вниз, влево, вправо)
5. Отрисовка игрового поля происходит каждый ход игрока (тем самым создается иллюзия непрерывности игры)
6. Как только игрок наступает на клетку с яблоком, переменная score увеличивается на 1, яблоко исчезает.
7. Игра заканчивается как только игрок соберет все яблочки.
** стены (процерно генерируемые лабиринты)
** перерисовка сразу после нажатия клавиши (без дополнительного Enter)
"""
# импорты библиотек
import os
import json

# импорты из вспомогательных файлов
from helpers.movements import go_up, go_down, go_left, go_right
from helpers.field import field_generation, field_output
from helpers.utilities import counter_apples, get_key

with open('data/text_for_game.json', 'r') as text:
    data = json.load(text)


def main():
    print(data['start'])
    len_row, len_column = map(int, input(data['input_param_of_field']).split())

    field = field_generation(row=len_row, column=len_column)
    user_position = [0, 0]
    user_data = [0, counter_apples(field)]  # score, count_apples

    while True:
        # вывод поля
        field_output(
            score=user_data[0],
            field=field,
            len_column=len_column
        )

        if user_data[1] == 0:
            print(data['win'])
            break

        # обработка нажатия
        print(data['start_doing'])
        key = get_key()
        if str(key) == "b'w'":
            os.system('cls')
            go_up(
                field=field,
                position=user_position,
                data=user_data
            )
        elif str(key) == "b's'":
            os.system('cls')
            go_down(
                field=field,
                position=user_position,
                data=user_data,
                len_row=len_row
            )
        elif str(key) == "b'd'":
            os.system('cls')
            go_right(
                field=field,
                position=user_position,
                data=user_data,
                len_column=len_column
            )
        elif str(key) == "b'a'":
            os.system('cls')
            go_left(
                field=field,
                position=user_position,
                data=user_data
            )
        elif str(key) == "b'q'":
            print(data['end_game'])
            break
        else:
            print(data['dont_understand'])


if __name__ == '__main__':
    main()
