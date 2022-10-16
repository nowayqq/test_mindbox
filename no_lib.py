from sum_dig import sum_of_digits


def group_score(arr, n_customers):

    unique_groups = dict()

    for i in range(n_customers):
        if arr[i] not in unique_groups:
            unique_groups[arr[i]] = 1
        else:
            unique_groups[arr[i]] += 1

    return dict(sorted(unique_groups.items(), key=lambda value: value[1]))


data = [7412567, 7412576, 12576, 12554, 888431]
groups = []

for item in data:
    groups.append(sum_of_digits(item))

print(groups)
print(group_score(groups, len(groups)))
