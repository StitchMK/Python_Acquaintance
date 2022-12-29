# 1. Вычислить число c заданной точностью d

from decimal import *

number = float(input('Enter a real number: '))
accuracy = float(input('Enter the required accuracy "0.0001": '))

print(Decimal(number))
modified_number = Decimal(number) + Decimal(accuracy)
print(modified_number)



