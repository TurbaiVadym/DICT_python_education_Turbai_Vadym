

# ввод пполей матрицы, в данном случае пустая
def player_input():
    input_list = "_" * 9
    print("----------------")
    return list(input_list)
"""
Ничего не передаем. Создает пустое поле для игры.
Отдает список из элементов поля.
"""

# вывод матрицы
def matrix_output(input_list):

    for _ in range (1):
        print(f"""|{input_list[0]} {input_list[1]} {input_list[2]}|""")
        print(f"""|{input_list[3]} {input_list[4]} {input_list[5]}|""")
        print(f"""|{input_list[6]} {input_list[7]} {input_list[8]}|""")
        print("""----------------""")
"""
input_list - хранит значения поля. Выводим в формате 3Х3
Ничего не возвращает
"""


# проверка состояния игры
def game_analysis(input_list):

    x_num = 0
    o_num = 0
    xwin = None
    owin = None

    for i in range(len(input_list)):
        if input_list[i] == 'X':
            x_num += 1

    for i in range(len(input_list)):
        if input_list[i] == 'O':
            o_num += 1

# Блок проверки по горизонтали (win)
    for i in range(0, 7, 3):  # Индексы 0, 3, 6 (т.е. начинаем с 0, проверяем 0-2, 3-5, 6-8)
        if input_list[i] == input_list[i + 1] == input_list[i + 2]:
            if input_list[i] == 'X':
                xwin = True
            elif input_list[i] == 'O':
                owin = True
# Блок проверки по вертикали (win)
    for i in range(3):  # Индексы 0, 1, 2 (проверяем столбцы 0-3-6, 1-4-7, 2-5-8)
        if input_list[i] == input_list[i + 3] == input_list[i + 6]:
            if input_list[i] == 'X':
                xwin = True
            elif input_list[i] == 'O':
                owin = True

# смотрим по диагонали
    if input_list[0] == input_list[4] == input_list[8] or input_list[2] == input_list[4] == input_list[6]:
        if input_list[4] == 'X':
            xwin = True
        elif input_list[4] == 'O':
            owin = True
# смотрим не выиграли ли оба (Impossible)
    if xwin and owin:
        print("Impossible")
        return True
# смотрим разницу X и O (Impossible)
    elif x_num - o_num > 1 or x_num - o_num > 1:
        print("Impossible.")
        return True
# выводим результат
    elif xwin:
        print("X wins")
        return True
    elif owin:
        print("O wins")
        return True
# смотрим состояние игры, если ничего из предыдущего, то ничья
    elif x_num + o_num == 9:
        print("Draw")
        return True
# смотрим количество игр (Not finished)
    elif x_num + o_num != 9:
        print("Game not finished yet.")
    return False
"""
Передаём состояние поля каждый шаг игры.
Проверяет линии на условия победы, ничьи, невозможных состояний, записывает и выводит кто победил
Возвращает Истину, если игра завершилась иначе Ложь
"""

# выводим текущего игрока и считываем координаты
def input_coords(player):
    print(f"Now playing {player}.")
    coords = input(f"Please, enter coordinates (from 1 to 3) first - x, second - y:")
    return coords
"""
Передает текущего игрока - Player. Возвращает введенные кооординаты - coords
"""

# проверка координат
def coordinates_check(coords):
    coords_split = coords.split()
    if len(coords_split) != 2:
        print("You should enter two numbers!")
        return None

    if coords_split[0].isdigit() and coords_split[1].isdigit():
        x, y = map(int, coords_split)
        if 1 <= x <= 3 and 1 <= y <= 3:
            return x, y
        else:
            print("Coordinates should be from 1 to 3!")
            return None
    else:
        print("You should enter numbers!")
        return None
"""
Принимает координаты - coords. Проверяет, что это правильные числа, иначе выводит сообщения.
Числа правильные = отдает эти числа в виду двух переменных.
Неправильные - не отдает ничего.
"""

#проверка не заняты ли координаты
def occupacy_check(input_list, x, y):
    if input_list[(x - 1) * 3 + (y - 1)] != "_":
        print("This cell is occupied! Choose another one!")
        return True
    return False
"""
Принимает элементы игрового поля - input_list, координаты - x, y, введенные игроком.
Отдает Истину, если по координатам клетка занята.
Ложь, если не занята.
"""

# вписываем Х или О по введенным координатам
def step(input_list, coords, player):
    res = coordinates_check(coords)
    if res:
        x, y = res
        if not occupacy_check(input_list, x, y):
            input_list[(x - 1) * 3 + (y - 1)] = player
            return True
    return False
"""
Принимает элементы игрового поля, координаты, текущего игрока.
Если occupacy_check возвращает Ложь, записывает элемент в поле и возвращает Истину.
В другом случае отдает Ложь.
"""

# главная функция
def main():
    data = player_input()
    player = 'X'

    while True:
        matrix_output(data)
        user_coords = input_coords(player)
        if step(data, user_coords, player):
            matrix_output(data)
            end = game_analysis(data)
            if data.count('_') == 0 or end:
                break
            player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()