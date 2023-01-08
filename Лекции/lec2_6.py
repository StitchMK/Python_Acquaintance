# Кортежи
# Кортеж - это неизменяемый "список"

a = (3, 4, 5)
print(a)
print(a[0])
print(a[-1])

# для кортежа нельзя прописать значение отдельного элемента a[0] = 12, так как это неизменяемый список
# кортеж из одного элемента: a = (3,) 

for item in a:
    print(item)

##########

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g: {} b:{}'.format(red, green, blue))
# r:red g:green b:dlue