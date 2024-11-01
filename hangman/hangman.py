import random

#Вибирає випадкове слово
def choose_word(word_list):
    return random.choice(word_list)

#Виводе меню гри
def display_menu():
    return input("Type 'play' to play the game, 'exit' to quit: ")

#Ініціалізує приховане слово і кількість життів
def initialize_game(answer):
    return '-' * len(answer), 8

#Обновлює приховане слово якщо здогадка правильна
def update_hidden_answer(hidden_answer, answer, user_answer):
    for i in range(len(answer)):
        if answer[i] == user_answer:
            hidden_answer = hidden_answer[:i] + user_answer + hidden_answer[i + 1:]
    return hidden_answer

#Запускає гру
def play_game(answer):
    hidden_answer, lives = initialize_game(answer)
    guessed_letters = ""  # Зберігання вгаданих букв у рядку

    print('HANGMAN\n')
    print(hidden_answer)

    while lives > 0:
        user_answer = input("Guess the word: ")

        if len(user_answer) != 1:
            print('You should input a single letter.')
        elif not user_answer.islower():
            print('Please enter a lowercase English letter.')
        elif user_answer in guessed_letters:
            print("You've already guessed this letter.")
        else:
            guessed_letters += user_answer  # Додаємо букву у рядок вгаданих букв
            if user_answer in answer:
                hidden_answer = update_hidden_answer(hidden_answer, answer, user_answer)
                print(hidden_answer)
                if hidden_answer == answer:
                    print('You survived!')
                    return
            else:
                lives -= 1
                print(hidden_answer)
                print("That letter doesn't appear in the word.")

        if lives == 0:
            print('You lost!')

#Головна функція
def main():
    word_list = ['python', 'java', 'javascript', 'php']
    while True:
        menu_choice = display_menu()
        if menu_choice == 'play':
            answer = choose_word(word_list)
            play_game(answer)
        elif menu_choice == 'exit':
            break
        else:
            print("Invalid option. Please type 'play' or 'exit'.")


# Запуск гри
if __name__ == "__main__":
    main()






