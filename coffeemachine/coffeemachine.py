class CoffeeMachine:
    """
    Клас, що представляє кавомашину.

    Атрибути:
        money (int): Кількість грошей у кавомашині.
        cups_water (int): Кількість води (у мл).
        cups_milk (int): Кількість молока (у мл).
        cups_coffee_beans (int): Кількість кавових зерен (у грамах).
        disposable_cups (int): Кількість одноразових стаканчиків.
        state (str): Поточний стан кавомашини.
    """

    # Параметри кави як словники, а не окремі класи
    COFFEE_TYPES = {
        "espresso": {"cost": 4, "water": 250, "milk": 0, "coffee_beans": 16, "cups": 1},
        "latte": {"cost": 7, "water": 350, "milk": 75, "coffee_beans": 20, "cups": 1},
        "cappuccino": {"cost": 6, "water": 200, "milk": 100, "coffee_beans": 12, "cups": 1}
    }

    def __init__(self):
        """Ініціалізує кавомашину з початковими значеннями ресурсів."""
        self.money = 550
        self.cups_water = 400
        self.cups_milk = 540
        self.cups_coffee_beans = 120
        self.disposable_cups = 9
        self.state = "choosing_action"  # Поточний стан кавомашини

    def remaining(self):
        """Виводить поточний стан ресурсів кавомашини."""
        print(f"The coffee machine has:\n{self.money} UAH\n{self.cups_water} ml of water\n{self.cups_milk} ml of milk\n"
              f"{self.cups_coffee_beans} g of coffee beans\n{self.disposable_cups} of disposable cups")

    def buy(self, action):
        """
        Обробляє покупку кави.

        Параметри:
            action (str): Вибір користувача (1 - еспресо, 2 - латте, 3 - капучино, back - повернення в меню).
        """
        if action == "back":
            self.state = "choosing_action"
            return

        coffee_type = None
        if action == "1":
            coffee_type = "espresso"
        elif action == "2":
            coffee_type = "latte"
        elif action == "3":
            coffee_type = "cappuccino"
        else:
            print("Invalid choice")
            return

        coffee = self.COFFEE_TYPES[coffee_type]

        # Перевіряємо, чи вистачає ресурсів
        if (self.cups_water >= coffee["water"] and
            self.cups_milk >= coffee["milk"] and
            self.cups_coffee_beans >= coffee["coffee_beans"] and
            self.disposable_cups >= coffee["cups"]):

            # Оновлюємо ресурси
            self.money += coffee["cost"]
            self.cups_water -= coffee["water"]
            self.cups_milk -= coffee["milk"]
            self.cups_coffee_beans -= coffee["coffee_beans"]
            self.disposable_cups -= coffee["cups"]
            print("I have enough resources, making you a coffee!")
        else:
            print("Sorry, not enough resources!")

        self.state = "choosing_action"

    def fill(self, water, milk, coffee_beans, cups):
        """
        Поповнює ресурси кавомашини.
        """
        self.cups_water += water
        self.cups_milk += milk
        self.cups_coffee_beans += coffee_beans
        self.disposable_cups += cups
        self.state = "choosing_action"

    def take(self):
        """Виводить гроші з кавомашини."""
        print(f"I gave you {self.money} UAH")
        self.money = 0
        self.state = "choosing_action"

    def process_input(self, user_input):
        """
        Обробляє введення користувача.
        """
        if self.state == "choosing_action":
            if user_input == "buy":
                self.state = "choosing_coffee"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
            elif user_input == "fill":
                self.state = "filling"
                print("Write how many ml of water do you want to add:")
            elif user_input == "take":
                self.take()
            elif user_input == "remaining":
                self.remaining()
            elif user_input == "exit":
                return False
            else:
                print("Invalid action!")

        elif self.state == "choosing_coffee":
            self.buy(user_input)

        elif self.state == "filling":
            water = int(user_input)
            milk = int(input("Write how many ml of milk do you want to add:\n> "))
            coffee_beans = int(input("Write how many grams of coffee beans do you want to add:\n> "))
            cups = int(input("Write how many disposable cups of coffee do you want to add:\n> "))
            self.fill(water, milk, coffee_beans, cups)

        return True


def main():
    coffee_machine = CoffeeMachine()
    coffee_machine.remaining()

    while True:
        if coffee_machine.state == "choosing_action":
            action = input("Write action (buy, fill, take, remaining, exit):\n> ")
        else:
            action = input()

        if not coffee_machine.process_input(action):
            break


if __name__ == '__main__':
    main()