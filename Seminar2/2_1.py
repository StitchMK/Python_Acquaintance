# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов
# in
# >> 5
# out
# >> 1, -3, 9, -27, 81

def n_func():
    for i in range(int(input('Input your number, please: '))):
        print((-3) ** i, end = ' ')

n_func()