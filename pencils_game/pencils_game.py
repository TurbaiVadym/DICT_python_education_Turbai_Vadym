
import random

name1 = "Alex"
name2 = "Biba(Bot)"
pencils_limitation = 3

pencils = 0

def get_pencils():
    """
        Запрашивает у пользователя количество карандашей для игры.
        Возвращает:
            int: Количество карандашей.
    """
    while True:
        pencils_quant = input("How many pencils?\n> ")
        if pencils_quant.isnumeric():
            pencils = int(pencils_quant)
            if pencils > 0:
                return pencils
            else:
                print("The number of pencils should be positive.")
        else:
            print("The number of pencils should be numeric.")

def get_player():
    """
        Запрашивает у пользователя, какой игрок начинает игру.
        Возвращает:
            str: Имя игрока, который начинает.
    """
    while True:
        the_first = input(f"Who will be the first ({name1} or {name2})?\n> ")
        if the_first in [name1, name2]:
            return the_first
        else:
            print(f"Choose between '{name1}' and '{name2}'.")

def show(pencils_quant, the_first):
    """
        Выводит текущее состояние игры: количество карандашей и чья очередь.
        Аргументы:
            pencils_quant (int): Количество карандашей.
            the_first (str): Имя игрока, чья очередь.
    """
    print("| " * pencils_quant)
    print(f"{the_first}'s turn: ")

def bot_move(pencils):
    """
        Определяет ход бота в зависимости от количества карандашей.
        Если остался только 1 карандаш, бот берет его. В проигрышной позиции бот делает случайный ход.
        Аргументы:
            pencils (int): Количество карандашей.
        Возвращает:
            int: Количество карандашей, которые берет бот.
    """
    if pencils == 1:
        return 1
    elif pencils % 4 == 0:
        return random.randint(1,3)
    elif pencils % 4 == 1:
        return 3
    elif pencils % 4 == 2:
        return 2
    elif pencils % 4 == 3:
        return 1

def player(pencils):
    """
        Запрашивает у пользователя количество карандашей, которые он хочет взять.
        Аргументы:
            pencils (int): Количество карандашей на столе.
        Возвращает:
            int: Количество карандашей, которые берет пользователь.
    """
    while True:
        picked_pencils = input("> ")
        if picked_pencils.isnumeric():
            picked_pencils = int(picked_pencils)
            if picked_pencils in [1, 2, 3]:
                if picked_pencils <= pencils:
                    return picked_pencils
                else:
                    print("Too many pencils were taken!")
            else:
                print("Possible values: '1', '2' or '3'.")
        else:
            print("Possible values: '1', '2' or '3'.")

# def game(pencils, current_player):
def main():
    """
        Основная функция игры.
    """
    pencils = get_pencils()
    current_player = get_player()

    while pencils > 0:
        show(pencils, current_player)

        if current_player == name2:
            picked_pencils = bot_move(pencils)
            print(f"> {picked_pencils}")
        else:
            picked_pencils = player(pencils)

        pencils -= picked_pencils

        if pencils == 0:
            if current_player == name1:
                print(f"{name2} won!")
            else:
                print(f"{name1} won!")
            break

        if current_player == name1:
            current_player = name2
        else:
            current_player = name1

if __name__ == '__main__':
    main()
