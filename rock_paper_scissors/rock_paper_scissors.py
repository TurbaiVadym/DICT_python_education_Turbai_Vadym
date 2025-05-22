
import random

# Варіанти гри за замовчуванням
default_options = ["rock", "paper", "scissors"]


def load_rating(name):
    """Завантажує рейтинг користувача з файлу rating.txt.

    Функція відкриває файл 'rating.txt' у режимі читання та шукає рядок,
    що починається з імені користувача. Якщо ім'я знайдено, повертає
    відповідний рейтинг. Якщо файл не знайдено або ім'я не знайдено,
    повертає 0.

    Args:
        name (str): Ім'я користувача, рейтинг якого потрібно завантажити.

    Returns:
        int: Поточний рейтинг користувача або 0, якщо рейтинг не знайдено.
    """
    try:
        with open("rating.txt", "r", encoding="utf-8") as f:
            for line in f:
                user, score = line.strip().split()
                if user == name:
                    return int(score)
    except FileNotFoundError:
        pass
    return 0  # Якщо файл не існує або ім'я не знайдено, повертаємо 0


def get_game_result(user_choice, computer_choice, options):
    """Визначає результат гри для користувача ('win', 'draw', 'lose').

    Функція порівнює вибір користувача та комп'ютера з урахуванням правил гри,
    визначених у списку 'options'. Перемога визначається за принципом:
    кожен елемент перемагає половину наступних елементів у циклічному списку.

    Args:
        user_choice (str): Вибір користувача.
        computer_choice (str): Вибір комп'ютера.
        options (list of str): Список можливих варіантів гри.

    Returns:
        str: Результат гри для користувача ('win', 'draw' або 'lose').
    """
    if user_choice == computer_choice:
        return "draw"

    # Знаходимо індекс вибору користувача
    user_idx = options.index(user_choice)

    # Створюємо список варіантів, які йдуть після user_choice, а потім ті, що перед ним
    rotated_options = options[user_idx + 1:] + options[:user_idx]

    # Перша половина перемагає user_choice, друга половина програє
    half = len(rotated_options) // 2
    winning_options = rotated_options[:half]  # Ці варіанти перемагають user_choice

    if computer_choice in winning_options:
        return "lose"
    return "win"


def main():
    """Основна функція програми, що запускає гру "Камінь, ножиці, папір" (або її розширену версію).

    Програма запитує ім'я користувача, завантажує його рейтинг (якщо є),
    пропонує ввести власні варіанти гри (якщо потрібно), а потім запускає
    ігровий цикл. Користувач вводить свій вибір, комп'ютер робить випадковий
    вибір, визначається результат, оновлюється рейтинг та виводиться повідомлення.
    Підтримуються спеціальні команди '!exit' для виходу та '!rating' для перегляду рейтингу.
    """
    # Запитуємо ім'я користувача
    name = input("Enter your name: > ").strip()
    print(f"Hello, {name}")

    # Завантажуємо початковий рейтинг
    rating = load_rating(name)

    # Запитуємо список опцій
    options_input = input("> ").strip()
    if options_input:
        options = [opt.strip() for opt in options_input.split(",")]
    else:
        options = default_options

    print("Okay, let's start")

    while True:
        # Зчитуємо вибір користувача
        user_choice = input("> ").strip().lower()

        # Перевіряємо спеціальні команди
        if user_choice == "!exit":
            print("Bye!")
            break
        elif user_choice == "!rating":
            print(f"Your rating: {rating}")
            continue

        # Перевіряємо, чи вибір користувача є дійсним
        if user_choice not in options:
            print("Invalid input")
            continue

        # Комп'ютер обирає випадковий варіант
        computer_choice = random.choice(options)

        # Визначаємо результат гри
        result = get_game_result(user_choice, computer_choice, options)

        # Оновлюємо рейтинг і виводимо результат
        if result == "win":
            rating += 100
            print(f"Well done. The computer chose {computer_choice} and failed")
        elif result == "draw":
            rating += 50
            print(f"There is a draw ({computer_choice})")
        else:  # result == "lose"
            print(f"Sorry, but the computer chose {computer_choice}")


if __name__ == "__main__":
    main()