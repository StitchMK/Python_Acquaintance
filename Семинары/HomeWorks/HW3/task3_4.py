# 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform

def random_real_nums(len_list):
    list_real_nums = []
    if len_list < 0:
        len_list *= -1
    
    for i in range(len_list):
        list_real_nums.append(round(uniform(1, len_list), 3))
    
    return list_real_nums

def min_and_max(my_list: list):
    min_num = max_num = my_list[0] % 1

    for i in range(1, len(my_list)):
        num = my_list[i] % 1

        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    
    difference = round((max_num - min_num), 3)

    print(f'Max: {round(max_num, 3)}, Min: {round(min_num, 3)}')
    print(f'The difference between the max and min fractional part is: {difference}')
    return difference

my_list = random_real_nums((int (input('Input the length of your list: '))))
print(my_list)
min_and_max(my_list)

