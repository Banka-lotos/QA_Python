def calculator():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            operation = input("Выберите операцию (+, -, *, /): ")

            if operation == '+':
                print("Результат:", num1 + num2)
            elif operation == '-':
                print("Результат:", num1 - num2)
            elif operation == '*':
                print("Результат:", num1 * num2)
            elif operation == '/':
                
                if num2 == 0:
                    print("Ошибка: деление на ноль")
                else:
                    print("Результат:", num1 / num2)
            else:
                print("Ошибка: Неверная операция")
        except ValueError:
            print("Ошибка: Введите числа корректно")
        except Exception as e:
            print("Ошибка:", e)

        choice = input("Хотите продолжить? (да/нет): ")
        if choice.lower() != 'да':
            break

calculator()