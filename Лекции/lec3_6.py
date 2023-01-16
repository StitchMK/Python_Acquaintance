#  Фильтр

data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data)) # или : x%2 == 0
print(res)