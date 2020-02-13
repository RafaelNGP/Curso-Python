# determine if a list is sorted

items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def is_sorted_brute(item_list):
    # "BRUTE FORCE" Method
    for i in range(len(item_list) - 1):
        if item_list[i] > item_list[i+1]:
            return False
    return True


def is_stored_all(item_list):
    return all(item_list[i] <= item_list[i+1] for i in range(len(item_list)-1))


print(is_sorted_brute(items1))
print(is_sorted_brute(items2))
print()
print(is_stored_all(items1))
print(is_stored_all(items2))
