def calc(oper, num1, num2):
    try:
        if oper == '+':
            return num1 + num2
        elif oper == '-':
            return num1 - num2
        elif oper == '*':
            return num1 * num2
        elif oper == '/':
            if num2 == 0:
                raise ZeroDivisionError("делить нельзя")
            return num1 / num2
        else:
            raise ValueError("Неверная операция")
    except (ValueError, ZeroDivisionError) as d:
        return str(d)

    

#print (calc('+',5,3)) #ожидаемое 8
#print (calc('-',5,3)) #ожидаемое 2
#print (calc('*',5,3)) #ожидаемое 15
#print(calc('/',10,0)) #ожидаю обработку
#print(calc('?',5,3)) #ожидаю увидеть обработку неверная операция
