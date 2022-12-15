# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

n = int(input('Enter the number of the day of the week: '))
if n == 6 or n == 7:
    print('Yes')
else:
    print('No')
