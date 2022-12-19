# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

numbers = []
n = int(input('Enter number of elements: '))
sum = 0

for i in range(1, n + 1):
    numbers.append((1 + 1 / i) ** i)
    sum += numbers[i]

print(numbers)
print(sum)