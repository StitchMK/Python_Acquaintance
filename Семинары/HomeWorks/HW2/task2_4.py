# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

numbers = []
n = int(input('Enter the value of N: '))
position_1 = int(input('Enter the position number one: '))
position_2 = int(input('Enter the position number two: '))

for i in range(- (n + 1), n):
    numbers.append(i + 1)

print(numbers)

if position_1 > (n * 2) or position_2 > (n * 2):
    print('There are no values for these indexes!')
else:
    product = numbers[position_1 - 1] * numbers[position_2 - 1]
    print(product)