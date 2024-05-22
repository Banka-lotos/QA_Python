#задача от 17,05 


def sum_of_dig(num):
    sum = 0
    while num != 0:
        last_digit = num % 10
        sum += last_digit
        num //= 10
    return sum

# пример
num = 2536
print("Sum of digits of", num, ":", sum_of_dig(num))