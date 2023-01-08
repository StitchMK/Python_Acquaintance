# Рекурсия

def fib(n):
    if n in [1, 2]:         # если попали в первй или второй элемент, возвращаем единицу
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

list = []
for e in range(1, 10):          # Смотрим список от первого до десятого элемента
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34