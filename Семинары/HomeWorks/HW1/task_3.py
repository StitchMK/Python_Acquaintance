# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Enter the x-coordinate of the point unequal to zero: '))
y = int(input('Enter the y-coordinate of the point unequal to zero: '))
c = 0

if x > 0 and y > 0:
    c = 1
    print('The point is located in the first quarter of the coordinate plane:', c)
elif x < 0 and y > 0:
    c = 2
    print('The point is located in the second quarter of the coordinate plane:', c)
elif x < 0 and y < 0:
    c = 3
    print('The point is located in the third quarter of the coordinate plane:', c)
elif x > 0 and y < 0:
    c = 4
    print('The point is located in the fourth quarter of the coordinate plane:', c)
else:
    print('The coordinates are entered incorrectly')
