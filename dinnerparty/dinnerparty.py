import random

# Зчитує кількість друзів
def display():
    return input('Enter the number of friends joining (including you):\n')

# Перевіряє кількість друзів, чи це цифра та чи не дорівнює вона нулю
# friends_num - кількість друзів включаєчи користувача
def friends_num_check(friends_num):
    if not friends_num.isdigit() or int(friends_num) == 0:
        return False
    else: return True

# Зчитує загальну кількість грошей
def get_amount():
    return input('Enter the total amount:\n')

# Рахує кількість грошей для кожного
# friends_num, total_amount - загальні грощі
def calculations(total_amount, friends_num):
    return round(float(total_amount) / int(friends_num), 2)

# Зчитує імена друзів і користувача
# friends_num
def get_friends_name(friends_num):
    friends_name = list()
    for i in range(int(friends_num)):
        friends_name.append(input())
    return friends_name

"""
Створює словник з друзів та грошей, якими вони повинні скинутись
friends_dict - словник друзі-гроші на кожного, friends_num, friends_name - пустий список для імен друзів,
amount_per_one - кількість грошей для кожного
"""
def friends_dict_creation (friends_dict, friends_num, friends_name, amount_per_one):
    for i in range(int(friends_num)):
        friend = friends_name[i]
        friends_dict[friend] = friends_dict.get(friend, amount_per_one)
    return friends_dict

# Запитує про функцію щасливчик, вибирає щасливчика або не робить нічого 
def question_lucky(friends_dict):
    lucky_input = input("Do you wont to use 'Who is lucky' feature? Yes/No:\n").lower()
    if lucky_input == "yes":
        lucky_friend = random.choice(list(friends_dict.keys()))
        print(f"{lucky_friend} is the lucky one!")
        return lucky_friend
    else:
        print("Noone is going to be lucky.")
        print(friends_dict)
    return False

"""
friends_dict, lucky_friend - і'мя того самого щасливчика, total_amount, friends_num, friends_name - список імен друзів
"""
def recalculation(friends_dict, lucky_friend, total_amount, friends_num, friends_name):
    new_amount_per_one = round(float(total_amount) / (int(friends_num) - 1), 2)
    for i in range(int(friends_num)):
        friend = friends_name[i]
        friends_dict.update({friend: new_amount_per_one})
    friends_dict[lucky_friend] = 0
    return None

# головна функція
def main():

    friends_dict = dict()

    friends_num = display()

    if friends_num_check(friends_num):
        print('Enter the name of every friend (including you),each on a new line:')
        name = get_friends_name(friends_num)

        total_amount = get_amount()
        amount_per_one = calculations(total_amount, friends_num)
        friends_dict_creation(friends_dict, friends_num, name, amount_per_one)

        lucky = question_lucky(friends_dict, choose_list)

        if lucky:
            recalculation(friends_dict, lucky, total_amount, friends_num, name)
            print(friends_dict)
        else:
            pass
    else:
        print("No one is joining for the party.")


if __name__ == "__main__":
    main()




