# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factors(number):

    prim_fac = []
    num = 2

    while num * num <= number:
        if number % num == 0:
            prim_fac.append(num)
            number //= num
        else:
            num += 1

    if number > 1:
        prim_fac.append(number)
    
    return(prim_fac)

print(prime_factors(int (input('Input your number: '))))