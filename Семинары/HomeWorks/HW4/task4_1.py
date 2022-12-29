# 1. Вычислить число c заданной точностью d

from decimal import Decimal

number = float(input('Enter a real number: '))
accuracy = input('Enter the required accuracy "0.0001": ')

modified_number = Decimal(number).quantize(Decimal(accuracy))
print(modified_number)



