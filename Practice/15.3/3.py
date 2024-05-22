def sum_numbers(a):
    return sum(a)


def divide_sum(sum_result, divisor):
    try:
        return sum_result / divisor
    except ZeroDivisionError:
        return None


numbers = [1,2,3,4,5]
sum_res = sum_numbers(numbers)


if sum_res is not None:
    divisor = int(input())
    divisor_res = divide_sum(sum_res,divisor)
    if divisor_res is not None:
        print('результат', divisor_res)

