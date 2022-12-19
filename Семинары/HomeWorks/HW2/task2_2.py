# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N в виде списка.

number = int(input('Enter your number: '))
numbers = [1]

for i in range(1, number + 1):
    val = i * numbers[i-1]
    print(val)
    numbers.append(val)

print(numbers[1:])