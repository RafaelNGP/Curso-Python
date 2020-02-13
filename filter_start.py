items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable to perform a filter
filtro = dict()
# loop over each item and add to the hashtable
for key in items:
    filtro[key] = 0
# create aa set from the resulting keys in the hashtable
result = set(filtro.keys())
print(result)
