data_list = [1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 7, 8, 8, 9]
data_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
data_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print("Data list sebelum konversi:", data_list)
print("Data set sebelum konversi:", data_set)
print("Data tuple sebelum konversi:", data_tuple)

data_kelist = set(data_list)
print("\nData set dari list setelah konversi:", data_kelist)

data_keset = list(data_set)
print("\nData list dari set setelah konversi:", data_keset)

data_ketuple = set(data_tuple)
print("\nData set dari tuple setelah konversi:", data_ketuple)

data_tuple_set = tuple(data_set)
print("\nData tuple dari set setelah konversi:", data_tuple_set)