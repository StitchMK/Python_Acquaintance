# Словари - неупорядоченные коллекции произвольных объектов, с доступом по ключу

dictionary = []
dictionary = \
    {
       'up': '↑',
       'left': '←',
       'down': '→',
       'right': '↓'
    } 
print(dictionary)           # {'up': '↑', 'left': '←', 'down': '→', 'right': '↓'}
print(dictionary['left'])     # ←

for k in dictionary.keys():
    print(k)

for k in dictionary.values():
    print(k)

for v in dictionary:
    print(v)

for v in dictionary:
    print(dictionary[v])