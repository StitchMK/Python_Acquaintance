## Функции лямбда

## Первый примерчик:

# def f(x):
#    x**2

# g = f

# print(f(1))
# print(g(1))

## Второй примерчик:

# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# Третий примерчик:

# def calc1(x):
#     return x+10

# print(calc1(10))

# def calc2(x):
#     return x*10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

## Чеетвертый примерчик:

# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y  # это то же самое, что две строки выше

def mult(x, y):
    return x * y

def calc(op, a, b):
    print(op(a,b))
    # return op(a, b)

calc(mult, 4, 5)
calc(lambda x, y: x + y, 4, 5)