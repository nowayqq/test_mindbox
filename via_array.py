import numpy as np
from sum_dig import sum_of_digits


def group_score(arr):

    return np.asarray(np.unique(arr, return_counts=True)).T


data = np.array([7412567, 7412576, 12576, 12554, 888431])
groups = []

for item in data:
    groups.append(sum_of_digits(item))

print(group_score(groups))
