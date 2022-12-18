# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

number = input('Enter your number: ')
sum = 0

for i in range(0, len(number)):
    if number[i] != '.':
        sum += int(number[i])

print(sum)