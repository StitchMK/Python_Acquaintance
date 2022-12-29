# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

def non_repeating_elements(numbers):
    non_rep_elem = []

    for num in numbers:
        if num in non_rep_elem:
            continue
        else:
            non_rep_elem.append(num)
    
    return non_rep_elem

def filling_array(number):
    new_array = []

    for i in range(number):
        new_array.append(int(input()))

    return new_array

number = int(input('Enter the number of items in your lists: '))
primary_array = filling_array(number)
print(primary_array)
print(non_repeating_elements(primary_array))