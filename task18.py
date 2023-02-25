# Задача 18: Требуется найти в массиве из случайных чисел (от 1 до N) самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. Последняя строка содержит число X
# 
# *Пример:*
# 
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random


def find_all_closest_numbers(smallest_difference, random_numbers):
    closest_numbers = []
    for current_number in random_numbers:
        difference = abs(number_x - current_number)
        if difference == smallest_difference and current_number not in closest_numbers:
            closest_numbers.append(current_number)
    return closest_numbers


def find_the_smallest_difference(number_x, random_numbers):
    smallest_difference = number_x
    for current_number in random_numbers:
        difference = abs(number_x - current_number)
        if difference <= smallest_difference and current_number != number_x:
            smallest_difference = difference
    return smallest_difference


number_n = int(input('Введите количество элементов (N) в массиве: '))
number_x = int(input('Введите число (X): '))
random_numbers = [random.randint(1, number_x * 2) for i in range(1, number_n + 1)]
print(*random_numbers)
smallest_difference = find_the_smallest_difference(number_x, random_numbers)
closest_numbers = find_all_closest_numbers(smallest_difference, random_numbers)
print('->', *closest_numbers)
