# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def product_of_num(len_list):
    new_list = sample(range(1, len_list * 2), k=len_list)
    print(new_list)
    product_list = []
    if len_list % 2 == 0:
        n = len_list / 2
    else:
        n = int(len_list / 2) + 1
    print(n)

    for i in range(0, n):
        product_num = new_list[i] * new_list[len_list - 1 - i]
        i += 1
    print(new_list[i])
    print(new_list[len_list - 1 - i])
    print(product_num)

#        product_list[n] = product_num
#        n += 1

#    return product_list

print(product_of_num(int (input('Input the length of your list: '))))
