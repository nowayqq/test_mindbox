import pandas as pd
from sum_dig import sum_of_digits


# реализация через pandas
def group_score(df):

    return df.groupby('group').count()


data = pd.read_csv('data.csv')
data['group'] = 0

for i in range(len(data.ID)):
    data.loc[:, 'group'][i] = sum_of_digits(data.loc[:, 'ID'][i])

print(data)
print(group_score(data))
