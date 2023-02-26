# 21. Напишите программу для печати всех уникальных значений в словаре.
# { 1:2, 3:4 , 2:2 } -> 4,2

some_dict = {1:2, 3:4, 2:2}
some_list = []
for v in some_dict.values():
    some_list.append(v)
some_set = set(some_list)
print(some_dict, '->', *set(some_set))