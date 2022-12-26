# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def binary_num(number):
    bin_num = []

    while number > 0:
        bin_num.insert(0, number % 2)
        number = number // 2

    print(*bin_num)

binary_num(int (input('Input your number: ')))