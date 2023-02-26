# 19. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# 1 2 3 4 5
# K = 3 -> 3 4 5 1 2

import random

number_n = int(input('Введите количество элементов N в массиве: '))
number_k = int(input('Введите число K: '))
random_numbers = [random.randint(1, 10) for i in range(number_n)]
print('Последовательность: ', *random_numbers)

if number_k >= number_n:
    while number_k >= number_n:
        number_k = number_k - number_n

temp = 0
for _ in range(number_k):
    temp = random_numbers.pop()
    random_numbers.insert(0, temp)
print('Сдвинутая последовательность: ', *random_numbers)
