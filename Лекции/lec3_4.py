def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x%2, res)
res = select(lambda x: (x, x ** 2),res)
print(res)

# С использованием map():

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x%2, res)
res = list(map(lambda x: (x, x ** 2),res))
print(res)

# С использованием filter():

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x, x ** 2),res))
print(res)