# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
#    где k принимает значения от 1 до n включительно.

numbers = []
n = int(input('Enter the langth of list '))

for k in range(1, n + 1):
    numbers.append(3 * k + 1)

print(numbers)