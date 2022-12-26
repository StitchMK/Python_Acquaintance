# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample
import math

def product_of_num(len_list):
    new_list = sample(range(1, len_list * 2), k=len_list)
    print(new_list)
    product_list = []
    n = int(len_list / 2)


    for i in range(0, n):
        product_list.append(new_list[i] * new_list[len_list - 1 - i])
    if len_list % 2 != 0:
        product_list.append(new_list[(math.ceil(len_list / 2 - 1))])
        
    print(product_list)

print(product_of_num(int (input('Input the length of your list: '))))
