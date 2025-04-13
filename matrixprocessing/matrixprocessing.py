def menu():
    """
    Виводить меню з опціями для операцій з матрицями та повертає вибір користувача.
    :return: рядок з обраною опцією
    """
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = input("Your choice: > ")
    return choice

def matrix_input():
    """
    Зчитує матрицю з вводу користувача.
    :return: список списків (матриця)
    :raises ValueError: якщо введено неправильну кількість чисел у рядку
    """
    # Зчитуємо розміри матриці
    a, b = map(int, input().strip().split())
    print(f"Got size {a},{b}")

    matrix = []
    for i in range(a):
        # Зчитуємо рядок матриці
        row = list(map(int, input().strip().split()))
        if len(row) != b:
            raise ValueError(f"Expected {b} numbers in row {i+1}, got {len(row)}")
        matrix.append(row)
    print("Matrix read:")
    return matrix

def addition():
    """
    Виконує додавання двох матриць та виводить результат.
    """
    # Зчитуємо першу матрицю
    matrix1 = matrix_input()
    # Зчитуємо другу матрицю
    matrix2 = matrix_input()

    # Перевіряємо, чи можна додати матриці
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("ERROR")
        return

    rows, cols = len(matrix1), len(matrix2[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Додаємо відповідні елементи
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    # Виводимо результат
    for row in result:
        print(*row)

def multiply_by_constant():
    """
    Множить матрицю на константу та виводить результат.
    """
    # Зчитуємо матрицю
    matrix = matrix_input()
    # Зчитуємо константу
    constant = int(input())

    # Множимо матрицю на константу
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j] * constant)
        result.append(row)

    # Виводимо результат
    for row in result:
        print(*row)

def multiplication():
    """
    Виконує множення двох матриць та виводить результат.
    """
    print("Enter size of first matrix: > ", end="")
    matrix_a = matrix_input()
    print("Enter size of second matrix: > ", end="")
    matrix_b = matrix_input()

    # Перевіряємо, чи можливо перемножити матриці
    if len(matrix_a[0]) != len(matrix_b):
        print("The operation cannot be performed.")
        return

    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            mul_res = 0
            for k in range(len(matrix_a[0])):
                # Обчислюємо елемент результату
                mul_res += matrix_a[i][k] * matrix_b[k][j]
            row.append(mul_res)
        result.append(row)

    print("The result is:")
    for row in result:
        print(*row)

def transposition():
    """
    Транспонує матрицю за вибраним методом та виводить результат.
    """
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = input("Your choice: > ")

    print("Enter matrix size: > ", end="")
    matrix = matrix_input()

    result = []
    if choice == "1":  # Транспонування по головній діагоналі
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            result.append(row)
    elif choice == "2":  # Транспонування по побічній діагоналі
        for j in range(len(matrix[0]) - 1, -1, -1):
            row = []
            for i in range(len(matrix) - 1, -1, -1):
                row.append(matrix[i][j])
            result.append(row)
    elif choice == "3":  # Транспонування по вертикальній лінії
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0]) - 1, -1, -1):
                row.append(matrix[i][j])
            result.append(row)
    elif choice == "4":  # Транспонування по горизонтальній лінії
        for i in range(len(matrix) - 1, -1, -1):
            row = []
            for j in range(len(matrix[0])):
                row.append(matrix[i][j])
            result.append(row)
    else:
        print("Invalid choice.")
        return

    print("The result is:")
    for row in result:
        print(*row)

def determinant(matrix):
    """
    Обчислює визначник квадратної матриці рекурсивно.
    :param matrix: вхідна матриця (список списків)
    :return: значення визначника або None, якщо матриця не квадратна
    """
    # Перевіряємо, чи матриця квадратна
    if len(matrix) != len(matrix[0]):
        return None

    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        # Формула для матриці 2x2: ad - bc
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        minor = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    # Формуємо мінор, виключаючи j-й стовпець
                    row.append(matrix[i][k])
            minor.append(row)
        # Додаємо вклад елемента до визначника
        det += matrix[0][j] * ((-1) ** j) * determinant(minor)
    return det

def calculate_determinant():
    """
    Зчитує матрицю та виводить її визначник.
    """
    matrix = matrix_input()
    det = determinant(matrix)
    if det is None:
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        print(det)

def minor_matrix(matrix, i, j):
    """
    Створює мінор матриці, виключаючи i-ий рядок і j-ий стовпець.
    :param matrix: вхідна матриця
    :param i: індекс рядка для виключення
    :param j: індекс стовпця для виключення
    :return: мінор (список списків)
    """
    minor = []
    for r in range(len(matrix)):
        if r == i:
            continue
        row = []
        for c in range(len(matrix[0])):
            if c != j:
                row.append(matrix[r][c])
        minor.append(row)
    return minor

def inverse():
    """
    Обчислює обернену матрицю та виводить її.
    """
    print("Enter matrix size: > ", end="")
    matrix = matrix_input()

    # Перевіряємо, чи матриця квадратна
    if len(matrix) != len(matrix[0]):
        print("This matrix doesn't have an inverse.")
        return

    # Обчислюємо визначник
    det = determinant(matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return

    n = len(matrix)
    algebraic_complement = []
    for i in range(n):
        row = []
        for j in range(n):
            # Обчислюємо алгебраїчне доповнення
            minor = minor_matrix(matrix, i, j)
            cofactor = ((-1) ** (i + j)) * determinant(minor)
            row.append(cofactor)
        algebraic_complement.append(row)

    # Транспонуємо матрицю алгебраїчних доповнень
    adjoin_matrix = []
    for j in range(n):
        row = []
        for i in range(n):
            row.append(algebraic_complement[i][j])
        adjoin_matrix.append(row)

    # Ділимо на визначник для отримання оберненої матриці
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(adjoin_matrix[i][j] / det)
        result.append(row)

    print("The result is:")
    for row in result:
        print(*[f"{x:.2f}" for x in row])

def main():
    """
    Основна функція, яка керує вибором операцій через меню.
    """
    while True:
        choice = menu()
        if choice == "1":
            addition()
        elif choice == "2":
            multiply_by_constant()
        elif choice == "3":
            multiplication()
        elif choice == "4":
            transposition()
        elif choice == "5":
            calculate_determinant()
        elif choice == "6":
            inverse()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()