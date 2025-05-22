
import random


def generate_task(level):
    """Генерує математичне завдання заданого рівня складності.

    Args:
        level (int): Рівень складності завдання (1 або 2).
                     1 - прості операції (+, -, *) з числами від 2 до 9.
                     2 - зведення в квадрат цілих чисел від 11 до 29.

    Returns:
        tuple: Кортеж, що містить рядок із завданням та правильну відповідь (int).

    Raises:
        ValueError: Якщо передано непідтримуваний рівень складності.
    """
    if level == 1:
        # Рівень 1: прості операції з числами 2-9
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:  # operation == '*'
            correct_answer = num1 * num2
        return f"{num1} {operation} {num2}", correct_answer
    elif level == 2:
        # Рівень 2: зведення в квадрат чисел 11-29
        num = random.randint(11, 29)
        correct_answer = num ** 2
        return str(num), correct_answer
    else:
        raise ValueError(f"Unsupported level: {level}")


def get_user_answer():
    """Отримує відповідь користувача з консолі та перевіряє її формат.

    Користувач повинен ввести ціле число. У випадку некоректного формату
    виводиться повідомлення про помилку, і запит повторюється.

    Returns:
        int: Відповідь користувача у вигляді цілого числа.
    """
    while True:
        try:
            user_answer = input("> ")
            return int(user_answer)
        except ValueError:
            print("Incorrect format.")


def get_level():
    """Запитує у користувача бажаний рівень складності тесту.

    Пропонує користувачеві обрати рівень 1 або 2 та перевіряє введене значення.
    У випадку некоректного введення виводиться повідомлення про помилку,
    і запит повторюється.

    Returns:
        int: Обраний рівень складності (1 або 2).
    """
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        try:
            level = int(input("> "))
            if level in [1, 2]:
                return level
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")


def save_result(name, correct_count, total_tasks, level):
    """Зберігає результати тесту користувача у файл 'results.txt'.

    Записує ім'я користувача, кількість правильних відповідей, загальну кількість
    завдань та рівень складності у файл 'results.txt'. Кожен результат
    записується на новому рядку.

    Args:
        name (str): Ім'я користувача.
        correct_count (int): Кількість правильних відповідей.
        total_tasks (int): Загальна кількість завдань у тесті.
        level (int): Рівень складності тесту (1 або 2).
    """
    level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
    result_line = f"{name}: {correct_count}/{total_tasks} in level {level} ({level_description}).\n"
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(result_line)


def main():
    """Основна функція програми, що запускає арифметичний тест.

    Запитує рівень складності, генерує задану кількість завдань,
    отримує відповіді користувача, перевіряє їх, виводить результати
    та пропонує зберегти їх у файл.
    """
    # Запитуємо рівень складності
    level = get_level()

    correct_count = 0
    total_tasks = 5

    # Задаємо 5 завдань
    for _ in range(total_tasks):
        # Генеруємо завдання
        task, correct_answer = generate_task(level)

        # Показуємо завдання користувачу
        print(task)

        # Отримуємо відповідь користувача
        user_answer = get_user_answer()

        # Перевіряємо відповідь
        if user_answer == correct_answer:
            print("Right!")
            correct_count += 1
        else:
            print("Wrong!")

    # Виводимо оцінку
    print(f"Your mark is {correct_count}/{total_tasks}.")

    # Запитуємо, чи зберегти результат
    save_choice = input("Would you like to save your result to the file? Enter yes or no: > ").strip().lower()
    if save_choice in ["yes", "y"]:
        name = input("What is your name?\n> ").strip()
        save_result(name, correct_count, total_tasks, level)
        print('The results are saved in "results.txt".')
    else:
        print("Exiting program.")


if __name__ == "__main__":
    main()