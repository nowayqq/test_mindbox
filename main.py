import pandas as pd


# реализация через pandas
def sum_of_digits(num):

    summ = 0

    while num > 0:
        digit = num % 10
        summ += digit
        num //= 10

    return summ


def group_score(df):

    return df.groupby('group').count()


data = pd.read_csv('data.csv')
data['group'] = 0

for i in range(len(data.ID)):
    data.loc[:, 'group'][i] = sum_of_digits(data.loc[:, 'ID'][i])

print(data)
print(group_score(data))
