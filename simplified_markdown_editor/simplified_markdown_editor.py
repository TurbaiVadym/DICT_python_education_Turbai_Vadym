
# Список доступних форматтерів
formatters = [
    "plain", "bold", "italic", "header", "link", "inline-code",
    "ordered-list", "unordered-list", "new-line"
]

# Список спеціальних команд #
special_commands = ["!help", "!done"]

# Зберігаємо Markdown-розмітку
markdown_output = []

def print_help():
    """Виводить довідку з доступними форматтерами та командами.

    Доступні форматтери відображаються у вигляді списку, розділеного пробілами.
    Спеціальні команди також відображаються у вигляді списку, розділеного пробілами.
    """
    print("Available formatters:", " ".join(formatters))
    print("Special commands:", " ".join(special_commands))

def print_markdown():
    """Виводить поточну Markdown-розмітку.

    Кожен елемент списку `markdown_output` виводиться на окремому рядку.
    """
    print("\n".join(markdown_output))

def save_to_file():
    """Зберігає Markdown-розмітку у файл output.md.

    Вміст списку `markdown_output` записується у файл "output.md",
    причому кожен елемент списку розміщується на новому рядку.
    Файл зберігається з кодуванням UTF-8.
    """
    with open("output.md", "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_output))

def format_text(formatter, text=None, level=None, label=None, url=None, rows=None):
    """Форматує текст відповідно до вибраного форматтера.

    Args:
        formatter (str): Назва форматтера, який потрібно застосувати.
        text (str, optional): Текст для форматування. Залежить від форматтера. Defaults to None.
        level (int, optional): Рівень заголовка (для форматтера "header"). Defaults to None.
        label (str, optional): Мітка для посилання (для форматтера "link"). Defaults to None.
        url (str, optional): URL-адреса для посилання (для форматтера "link"). Defaults to None.
        rows (list of str, optional): Список рядків для списків (для форматтерів "ordered-list", "unordered-list"). Defaults to None.

    Returns:
        str or list of str: Відформатований текст або список відформатованих рядків.

    Raises:
        ValueError: Якщо вказаний форматтер не підтримується.
    """

    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"**{text}**"
    elif formatter == "italic":
        return f"*{text}*"
    elif formatter == "inline-code":
        return f"`{text}`"
    elif formatter == "header":
        return f"{'#' * level} {text}"
    elif formatter == "link":
        return f"[{label}]({url})"
    elif formatter == "new-line":
        return ""
    elif formatter == "ordered-list":
        return [f"{i + 1}. {row}" for i, row in enumerate(rows)]
    elif formatter == "unordered-list":
        return [f"* {row}" for row in rows]
    else:
        raise ValueError("Formatter not supported yet")

def main():
    """Основна функція програми, що забезпечує інтерактивну роботу з користувачем."""
    while True:
        # Запитуємо форматтер у користувача
        formatter = input("Choose a formatter: > ").strip()

        # Перевіряємо, чи введено спеціальну команду
        if formatter == "!help":
            print_help()
            continue
        elif formatter == "!done":
            # Зберігаємо результат у файл перед виходом
            save_to_file()
            print("Exiting program.")
            break

        # Перевіряємо, чи введено відомий форматтер
        if formatter not in formatters:
            print("Unknown formatting type or command")
            continue

        # Обробка форматтерів
        try:
            if formatter == "new-line":
                markdown_output.append("")
            elif formatter == "header":
                # Запитуємо рівень заголовка
                level = input("Level: > ").strip()
                if not level.isdigit():
                    print("The level should be within the range of 1 to 6")
                    continue
                level = int(level)
                if level < 1 or level > 6:
                    print("The level should be within the range of 1 to 6")
                    continue
                # Запитуємо текст
                text = input("Text: > ").strip()
                markdown_output.append(format_text(formatter, text=text, level=level))
            elif formatter == "link":
                # Запитуємо label та URL
                label = input("Label: > ").strip()
                url = input("URL: > ").strip()
                markdown_output.append(format_text(formatter, label=label, url=url))
            elif formatter in ["ordered-list", "unordered-list"]:
                # Запитуємо кількість рядків
                num_rows = input("Number of rows: > ").strip()
                if not num_rows.lstrip('-').isdigit():
                    print("The number of rows should be greater than zero")
                    continue
                num_rows = int(num_rows)
                if num_rows <= 0:
                    print("The number of rows should be greater than zero")
                    continue
                # Запитуємо рядки
                rows = []
                for i in range(num_rows):
                    row = input(f"Row #{i + 1}: > ").strip()
                    rows.append(row)
                # Додаємо список до розмітки
                formatted_rows = format_text(formatter, rows=rows)
                markdown_output.extend(formatted_rows)
            else:
                # Запитуємо текст для інших форматтерів
                text = input("Text: > ").strip()
                markdown_output.append(format_text(formatter, text=text))

            # Виводимо поточну Markdown-розмітку
            print_markdown()

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()