# Функция map

# li = [x for x in range(1,20)]

# li = list(map(lambda x:x+10, li))

# print(li) 

## Второй примерчик

# data = list(map(int, input().split()))
# print(data)

#или
data = map(int, '1 2 3 4 555 6'.split()) # для ввода с клавиатуры: data = map(int, input().split())

for e in data:
    print(e)

print('--')

for e in data:
    print(e)

# если мы хотим два раза обращаться, то нужно сначала преобразовать в list:

data = list(map(int, '1 2 3 4 555 6'.split())) 

for e in data:
    print(e)

print('--')

for e in data:
    print(e)

