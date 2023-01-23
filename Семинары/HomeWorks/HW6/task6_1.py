# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. 
# Use comprehension.

from random import randint

def more_then(num):
    original_list = [randint(0, 100) for _ in range(num)]
    print(original_list)
    return [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]

print(more_then(int(input('Enter a number of elements: '))))