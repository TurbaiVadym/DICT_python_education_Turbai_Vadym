
import math
import argparse

def calculate_monthly_payment(principal, months):
    """Обчислює щомісячний платіж та останній платіж для безвідсоткового кредиту.
    Returns:
        float: щомісячний платіж
        float: останній платіж для безвідсоткового кредиту
    """
    payment = math.ceil(principal / months)
    last_payment = principal - (months - 1) * payment
    return payment, last_payment

def calculate_months(principal, monthly_payment):
    """Обчислює кількість місяців для погашення кредиту.
    Returns:
        int: кількість місяців
    """
    months = math.ceil(principal / monthly_payment)
    return months

def calculate_annuity_payment(principal, months, monthly_interest):
    """Обчислює щомісячний ануїтетний платіж.

    Args:
        principal (float): Основна сума кредиту.
        months (int): Кількість місяців для погашення.
        monthly_interest (float): Місячна процентна ставка.

    Returns:
        float: Щомісячний ануїтетний платіж.
    """
    x = math.pow(1 + monthly_interest, months)
    annuity_payment = principal * (monthly_interest * x) / (x - 1)
    return math.ceil(annuity_payment)

def calculate_principal(annuity_payment, months, monthly_interest):
    """Обчислює основну суму кредиту для ануїтетного платежу.

    Args:
        annuity_payment (float): Щомісячний ануїтетний платіж.
        months (int): Кількість місяців для погашення.
        monthly_interest (float): Місячна процентна ставка.

    Returns:
        float: Основна сума кредиту.
    """
    x = math.pow(1 + monthly_interest, months)
    principal = annuity_payment * (x - 1) / (monthly_interest * x)
    return math.floor(principal)

def calculate_months_for_annuity(principal, annuity_payment, monthly_interest):
    """Обчислює кількість місяців для ануїтетного платежу.

    Args:
        principal (float): Основна сума кредиту.
        annuity_payment (float): Щомісячний ануїтетний платіж.
        monthly_interest (float): Місячна процентна ставка.

    Returns:
        int: Кількість місяців, необхідних для погашення кредиту.
    """
    months = math.log(annuity_payment / (annuity_payment - monthly_interest * principal), 1 + monthly_interest)
    return math.ceil(months)

def calculate_differentiated_payments(principal, months, monthly_interest):
    """Обчислює диференційовані платежі.

    Args:
        principal (float): Основна сума кредиту.
        months (int): Кількість місяців для погашення.
        monthly_interest (float): Місячна процентна ставка.

    Returns:
        list: Список диференційованих щомісячних платежів.
    """
    payments = []
    for m in range(1, months + 1):
        payment = principal / months + monthly_interest * (principal - principal * (m - 1) / months)
        payments.append(math.ceil(payment))
    return payments

def months_to_years_and_months(months):
    """Перетворює кількість місяців у формат 'X років Y місяців'.

    Args:
        months (int): Загальна кількість місяців.

    Returns:
        str: Рядок у форматі 'X років Y місяців' або 'X місяців', або 'X років'.
    """
    years = months // 12
    remaining_months = months % 12
    if years == 0:
        return f"{remaining_months} months"
    elif remaining_months == 0:
        return f"{years} years"
    else:
        return f"{years} years and {remaining_months} months"

def main():
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment: 'annuity' or 'diff'")
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--periods", type=int, help="Number of months")
    parser.add_argument("--interest", type=float, help="Annual interest rate (in %)")
    parser.add_argument("--payment", type=float, help="Monthly payment")

    args = parser.parse_args()

    # Перевірка правильності параметрів
    if not args.type or args.type not in ["annuity", "diff"]:
        print("Incorrect parameters")
        return
    if args.interest is None:
        print("Incorrect parameters")
        return
    if args.type == "diff" and args.payment is not None:
        print("Incorrect parameters")
        return
    if sum(1 for arg in [args.principal, args.periods, args.interest, args.payment] if arg is not None) < 3:
        print("Incorrect parameters")
        return
    if any(arg is not None and arg < 0 for arg in [args.principal, args.periods, args.interest, args.payment]):
        print("Incorrect parameters")
        return

    # Обчислення номінальної процентної ставки
    monthly_interest = args.interest / (12 * 100)

    if args.type == "diff":
        # Диференційовані платежі
        payments = calculate_differentiated_payments(args.principal, args.periods, monthly_interest)
        total_payment = sum(payments)
        overpayment = total_payment - args.principal
        for i, payment in enumerate(payments, 1):
            print(f"Month {i}: payment is {payment}")
        print(f"Overpayment = {math.ceil(overpayment)}")

    elif args.type == "annuity":
        if args.payment is None:
            # Обчислення ануїтетного платежу
            annuity_payment = calculate_annuity_payment(args.principal, args.periods, monthly_interest)
            total_payment = annuity_payment * args.periods
            overpayment = total_payment - args.principal
            print(f"Your annuity payment = {annuity_payment}!")
            print(f"Overpayment = {math.ceil(overpayment)}")

        elif args.principal is None:
            # Обчислення основної суми кредиту
            principal = calculate_principal(args.payment, args.periods, monthly_interest)
            total_payment = args.payment * args.periods
            overpayment = total_payment - principal
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {math.ceil(overpayment)}")

        elif args.periods is None:
            # Обчислення кількості місяців
            months = calculate_months_for_annuity(args.principal, args.payment, monthly_interest)
            total_payment = args.payment * months
            overpayment = total_payment - args.principal
            print(f"It will take {months_to_years_and_months(months)} to repay this loan!")
            print(f"Overpayment = {math.ceil(overpayment)}")

if __name__ == "__main__":
    main()



