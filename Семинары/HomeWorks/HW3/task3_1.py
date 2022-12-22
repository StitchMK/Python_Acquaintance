# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def sum_of_odd_num(len_list):
    new_list = sample(range(1, len_list * 10), k=len_list)
    print(new_list)
    sum_of_odd = 0

    for i in range(0, len_list):
        if i % 2 == 0:
            sum_of_odd += new_list[i]

    return sum_of_odd

print(sum_of_odd_num(int (input('Input the length of your list: '))))
