# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import sample

def create_list (count, word = 'abc'):
    my_list = []

    for i in range(count):
        temp = sample(word, k=3)
        my_list.append(''.join(temp))
    
    return my_list

def find_word_index(new_word, my_list):
    if new_word in my_list and my_list.count(new_word) > 1:
        index_1 = my_list.index(new_word)
        print(my_list.index(new_word, index_1 + 1))
    else:
        print('-1')

first_list = create_list(int(input()))
print(first_list)

find_word_index(input(), first_list)