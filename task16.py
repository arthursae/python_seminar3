# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите искомое число: '))
random_numbers = [random.randint(1, x * 2) for i in range(1, n + 1)]
counter = 0
for number in random_numbers:
    if x == number:
        counter += 1
print(*random_numbers)
print('->', counter)