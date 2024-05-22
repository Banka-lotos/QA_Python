
def calc():
    while True:
        # Ввод операции
        oper = input("Выберите операцию (+, -, *, /), или введите 'w' для выхода: ")

        # Проверка на выход
        if oper.lower() == 'w':
            print("Выход из калькулятора.")
            break
        
        # Ввод чисел
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Некорректный ввод чисел.")
            continue

        # Выполнение операции и вывод результата
        if oper == '+':
            result = num1 + num2
        elif oper == '-':
            result = num1 - num2
        elif oper == '*':
            result = num1 * num2
        elif oper == '/':
            # Проверка деления на ноль
            if num2 != 0:
                result = num1 / num2
            else:
                print("Ошибка: Деление на ноль!")
                continue
        else:
            print("Ошибка: Неверная операция!")
            continue

        print(f"Результат: {result}")

calc()