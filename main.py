import numpy as np
import pandas as pd


def sum_of_digits (num):

    summ = 0

    while num > 0:
        digit = num % 10
        summ += digit
        num //= 10

    return summ


data = pd.read_csv('data.csv')
data['group'] = 0

for i in range(len(data.ID)):
    data['group'][i] = sum_of_digits(data['ID'][i])

print(data)