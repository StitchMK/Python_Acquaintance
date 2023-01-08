def new_string(symbol, count):
    return symbol * count

print(new_string('!', 5))   # !!!!!
print(new_string('!'))      # TypeError missing 1 required ...

# Второй вариант (можно не указывать каждый раз цифру, по умолчанию она будет равна заданному числу)
# Количество аргументов по умолчанию не ограниено, но они должны описываться в конце

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5))   # !!!!!
print(new_string('!'))      # !!!
print(new_string(4))        # 12