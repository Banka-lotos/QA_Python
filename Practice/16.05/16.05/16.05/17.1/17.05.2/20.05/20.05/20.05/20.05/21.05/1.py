def i (num):
    i = []

    for num in numbers:
        if num % 3 ==0:
           i.append(num)
    return i

# Пример 
numbers = [12, 22, 33, 4, 105, 6, 7, 88, 39, 100]
result = i(numbers)
print(result)