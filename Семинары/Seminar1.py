# 1. Напишите программу, которая принимает на вход два числа
#    и проверяет, является ли одно число квадратом другого.

#n = int(input())
#m = int(input())

#if n == m ** 2 or m == n ** 2:
#    print('Yes')
#else:
#    print('No')


# Задача 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них (только положительные числа).

#number_max = 0

#for i in range (5):
#    number = int(input())
#    if number > number_max:
#        number_max = number

#print('Максимальное число из введенных:', number_max)

# Задача 3. Напишите программу, которая будет на вход принимать
#    число N и выводить числа от -N до N (положительные числа, для отрицательных - проверку)

#list(range(5, 25, 2))  #от, до, шаг

#def range_numbers_n():
#    n = int(input("Input your number: "))
#    print(*range(-n, n + 1))

#range_numbers_n()

# Задача 4. Напишите программу, которая будет принимать на вход дробь
#    и показывать первую цифру дробной части числа.

#n = float(input())
#n = n * 10 % 10
#print(int(n))

#второе решение:

#def check_first_num():
#    number = float(input("Input your number: "))
#    new_num = int(number * 10 % 10)
#    print(new_num)

#check_first_num()

# Задача 5. Напишите программу, которая принимает на вход число и проверяет,
#    кратно ли оно 5 и 10 или 15, но не 30.

#number = int(input("Input your number: "))
#if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and number % 30 != 0:
#    print('Yes')
#else:
#    print('No')

#Задача 6 (ДЗ). Пример проверки ложности утверждения (x ≡ z ) ∨ (x → (y ∧ z))

#print("x y z")
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            if (x == z or x <= y and z):
#                print(x, y, z)








