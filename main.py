import math

def calculator():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число (если вы хотите извлечь корень, введите '0'): "))
            print("Выберите операцию:")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("6. Извлечение квадратного корня (выполняется над первым числом)")
            operation = input("Введите номер операции (1/2/3/4/5/6): ")

            if operation == '1':
                print(f"Результат: {num1 + num2}")
            elif operation == '2':
                print(f"Результат: {num1 - num2}")
            elif operation == '3':
                print(f"Результат: {num1 * num2}")
            elif operation == '4':
                if num2 == 0:
                    print("Ошибка: Деление на ноль невозможно.")
                else:
                    print(f"Результат: {num1 / num2}")
            elif operation == '5':
                print(f"Результат: {num1 ** num2}")
            elif operation == '6':
                if num1 < 0:
                    print("Ошибка: Невозможно извлечь корень из отрицательного числа.")
                else:
                    print(f"Результат: {math.sqrt(num1)}")
            else:
                print("Ошибка: Неверный выбор операции.")

        except ValueError:
            print("Ошибка: Некорректный ввод. Введите числовые значения.")

        repeat = input("Хотите выполнить еще одну операцию? (да/нет): ")
        if repeat.lower() != 'да':
            break

calculator()
