# list = []

# for i in range(1, 101):
#     # if(i%2 == 0):
#         list.append(i)

# print(list)

def f(x):
    return x**3

list = [(i, f(i)) for i in range(1, 20) if i %2 == 0]
print(list)