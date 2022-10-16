def sum_of_digits(num):

    summ = 0

    while num > 0:
        digit = num % 10
        summ += digit
        num //= 10

    return summ