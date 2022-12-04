
    # 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
    # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

    # - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
    # - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

def sum_list(list, index, i):
    multiplier = list[index] * list[-i]
    print(multiplier)

def multiplier_list(list):
    print(list)
    index = 0
    i = 1
    if len(list) % 2 == 0:
        while index != len(list) / 2:
            sum_list(list, index, i)
            index += 1
            i += 1

    else:
        while index != len(list) // 2 + 1:
            sum_list(list, index, i)
            index += 1
            i += 1

print('Enter the list items separated by a space: ')
list = list(map(int, input().split()))

multiplier_list(list)
