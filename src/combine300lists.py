import ast

# Read the content of the file
file_path = '300DollarTest.txt'
lst = []
with open(file_path, 'r') as file:
    filepath = (file.readlines())
    for lst1 in filepath:
        if str(lst1) != '\n':
            lst = lst + eval(lst1)
# print(lst)
sorted_list = sorted(lst, key=lambda x: abs(x[1]), reverse=True)
unique_elements = set()

# Use a new list to store the result
result = []

for item in sorted_list:
    # Convert the inner tuple to a tuple so it can be used in a set
    inner_tuple = tuple(item[0])
    if inner_tuple not in unique_elements:
        # If the inner tuple is not in the set, add it to the set and append the whole item to the result list
        unique_elements.add(inner_tuple)
        result.append(item)

print(result[5000:len(result)])
f = open('top5000inds.txt', 'w')
f.write(str(result[0:5000]))
f.close()
print(len(result))
f = open('last5000inds.txt', 'w')
f.write(str(result[5000:len(result)]))
f.close()
print(len(result))