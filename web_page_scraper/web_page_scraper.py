
import requests
from bs4 import BeautifulSoup
import os
import string


def clean_filename(title):
    """Очищає заголовок статті для створення імені файлу.

    Видаляє знаки пунктуації та замінює пробіли на підкреслення.
    Прибирає подвійні підкреслення

    Args:
        title (str): Оригінальний заголовок статті

    Returns:
        str: Очищений заголовок, придатний для використання як ім'я файлу
    """
    # Видаляємо знаки пунктуації
    translator = str.maketrans('', '', string.punctuation)
    cleaned_title = title.translate(translator)
    # Замінюємо пробіли на підкреслення
    cleaned_title = cleaned_title.replace(' ', '_').strip()
    # Видаляємо подвійні підкреслення
    while '__' in cleaned_title:
        cleaned_title = cleaned_title.replace('__', '_')
    return cleaned_title


def fetch_page(url):
    """Завантажує сторінку та повертає об’єкт BeautifulSoup або None при помилці.

    Намагається отримати вміст сторінки за вказаним URL.
    У разі успіху повертає об'єкт BeautifulSoup для парсингу HTML.
    У разі помилки (наприклад, некоректний статус відповіді або проблема з мережею)
    виводить повідомлення про помилку та повертає None

    Args:
        url (str): URL-адреса сторінки для завантаження

    Returns:
        BeautifulSoup or None: Об'єкт BeautifulSoup, якщо сторінка успішно завантажена та розпарсена,
                                інакше None
    """
    try:
        response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'}, timeout=10)
        if response.status_code != 200:
            print(f"The URL {url} returned {response.status_code}!")
            return None
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching page {url}: {e}")
        return None


def extract_article_info(article, article_type):
    """Витягує заголовок і URL статті, якщо тип відповідає article_type.

    Шукає елемент 'span' з атрибутом 'data-test'='article.type' для визначення типу статті.
    Якщо тип статті відповідає заданому `article_type`, шукає тег 'a' з атрибутом
    'data-track-action'='view article' для отримання заголовка та URL статті

    Args:
        article (bs4.Tag): Об'єкт тегу BeautifulSoup, що представляє статтю.
        article_type (str): Бажаний тип статті для фільтрації

    Returns:
        tuple or None: Кортеж (title, article_url), якщо стаття відповідає критеріям,
                       інакше None
    """
    type_span = article.find('span', {'data-test': 'article.type'})
    if type_span and type_span.text.strip() == article_type:
        title_tag = article.find('a', {'data-track-action': 'view article'})
        if title_tag:
            title = title_tag.text.strip()
            article_url = 'https://www.nature.com' + title_tag['href']
            return title, article_url
    return None


def save_article_content(article_url, filename):
    """Завантажує вміст статті та зберігає у файл, повертає True при успіху.

    Виконує HTTP-запит до URL статті.
    Якщо запит успішний, парсить HTML, знаходить вміст основного тексту статті
    (елемент `div` з класом, що містить 'body'), і зберігає його у вказаний файл

    Args:
        article_url (str): URL-адреса статті для завантаження
        filename (str): Шлях до файлу, куди буде збережено вміст статті

    Returns:
        bool: True, якщо вміст статті успішно збережено, False в іншому випадку
    """
    try:
        article_response = requests.get(article_url, headers={'Accept-Language': 'en-US,en;q=0.5'}, timeout=10)
        if article_response.status_code != 200:
            print(f"Failed to fetch article {article_url}: {article_response.status_code}")
            return False
        article_soup = BeautifulSoup(article_response.content, 'html.parser')
        body_div = article_soup.find('div', class_=lambda x: x and 'body' in x)
        if not body_div:
            print(f"No body content found for article {article_url}")
            return False
        body_text = body_div.get_text(strip=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(body_text)
        return True
    except requests.RequestException as e:
        print(f"Error fetching article {article_url}: {e}")
        return False


def process_page(page, article_type, base_url):
    """Обробляє одну сторінку, повертаючи список збережених файлів.

    Створює директорію для поточної сторінки, завантажує її вміст.
    Для кожної статті на сторінці перевіряє її тип. Якщо тип відповідає,
    витягує заголовок і URL, очищає заголовок для імені файлу та зберігає
    вміст статті у текстовий файл у відповідній директорії

    Args:
        page (int): Номер сторінки для обробки.
        article_type (str): Тип статті, який потрібно відфільтрувати.
        base_url (str): Базовий URL для формування URL сторінки

    Returns:
        list: Список шляхів до файлів, які були успішно збережені
    """
    saved_files = []
    url = base_url.format(page)
    soup = fetch_page(url)
    if not soup:
        return saved_files

    os.makedirs(f"Page_{page}", exist_ok=True)
    articles = soup.find_all('article')
    for article in articles:
        article_info = extract_article_info(article, article_type)
        if article_info:
            title, article_url = article_info
            filename = f"Page_{page}/{clean_filename(title)}.txt"
            if save_article_content(article_url, filename):
                saved_files.append(filename)
    return saved_files


def save_articles_by_type_and_pages(pages, article_type):
    """Зберігає статті заданого типу з кількох сторінок у директорії Page_N.

    Ітерує по заданій кількості сторінок, викликаючи `process_page` для кожної.
    Збирає список усіх збережених файлів та виводить їх

    Args:
        pages (int): Кількість сторінок для обробки.
        article_type (str): Тип статті, яку потрібно зберегти
    """
    base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={}"
    all_saved_files = []

    for page in range(1, pages + 1):
        saved_files = process_page(page, article_type, base_url)
        all_saved_files.extend(saved_files)

    if all_saved_files:
        print(f"Saved articles: {all_saved_files}")
    else:
        print(f"No articles of type '{article_type}' found.")
    print("Saved all articles.")


def main():
    """Основна функція.

    Запитує у користувача кількість сторінок та тип статті.
    Виконує перевірку введених даних.
    Викликає функцію save_articles_by_type_and_pages для початку процесу завантаження
    """
    print("Enter number of pages:")
    try:
        pages = int(input("> "))
        if pages <= 0:
            print("Number of pages must be positive!")
            return
    except ValueError:
        print("Invalid input for number of pages!")
        return
    print("Enter article type:")
    article_type = input("> ").strip()
    if not article_type:
        print("Article type cannot be empty!")
        return
    save_articles_by_type_and_pages(pages, article_type)


if __name__ == "__main__":
    main()









