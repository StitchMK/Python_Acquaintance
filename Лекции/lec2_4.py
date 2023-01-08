# Звездочка вначале позволяет передать неограниченное количество аргументов

def concatenatio (*params):
    res: str = ''                       # res: int = 0 ## res = 0 (будет подсчитываться сумма элементов) 
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
print(concatenatio('a', '1'))           # a1
# print(concatenatio(1, 2, 3, 4))       # TypeError: ...