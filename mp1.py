import random as r

def mysubsets(myset):
    new = []
    allsets = []
    for i in range(1000):
        new = r.choices(myset, k=5)
        if sum(new) == 0:
            allsets.append(new.copy())  # Append a copy of the subset as a separate list
    return allsets

myset = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]
all_subsets = []
for i in range(10):
    all_subsets.extend(mysubsets(myset))


# Find the union of all distinct subsets
union_of_subsets = set(map(tuple, all_subsets))

print("Union of all distinct subsets:")
for subset in union_of_subsets:
    print(list(subset))
print(len(union_of_subsets))