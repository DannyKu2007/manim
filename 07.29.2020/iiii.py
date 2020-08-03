f = []
my_name_is_array = []
with open("array_for_my_name_is_array.txt") as f:
    for line in f:
        my_name_is_array.append([int(i) for i in line.split()])
print(my_name_is_array)
print()
