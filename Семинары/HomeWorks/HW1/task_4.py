# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

c = int(input('Enter the quarter of the coordinate plane: '))

if c == 1:
    print('In this quater x > 0 and y > 0')
elif c == 2:
    print('In this quater x < 0 and y > 0')
elif c == 3:
    print('In this quater x < 0 and y < 0')
elif c == 4:
    print('In this quater x > 0 and y < 0')
else:
    print('There is no such quarter')

