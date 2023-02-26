# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# 1 2 3 1 2 4 -> 4 (1 2 3 4)

some_list = [1,2,3,1,2,4]
unique_list = set(some_list)
print(some_list, '->', len(unique_list), unique_list)