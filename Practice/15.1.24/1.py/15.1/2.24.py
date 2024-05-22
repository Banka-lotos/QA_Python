try :
    num1 = float(input('введите первое число :'))
    num2 = float(input('введите второе число :'))
    result = num1 / num2
    print("Результат деления:", result)

except ValueError:
    print("Ошибка: введите числа")
except ZeroDivisionError:
    print('Ошибка: деление на 0 невозможно')
    