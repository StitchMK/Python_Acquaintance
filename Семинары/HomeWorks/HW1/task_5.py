# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

xa = int(input('Enter the x-coordinate of the point A: '))
ya = int(input('Enter the y-coordinate of the point A: '))
xb = int(input('Enter the x-coordinate of the point B: '))
yb = int(input('Enter the y-coordinate of the point B: '))

distance = round((((xa - xb) ** 2 + (yb - ya) ** 2) ** 0.5), 3)

print('The distance between your points is: ', distance)


