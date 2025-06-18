num_1 = [2, 8, 9, 48, 8, 22, -12, 2]
num_2 = [x + 2 for x in num_1]
num_3 = [x for x in num_2 if x > 8]
print(num_1)
unique_array = list(set(num_3))
print(unique_array)