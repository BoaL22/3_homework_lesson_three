  
    # 1'. Задайте список из нескольких чисел. 
    # Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

    # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print('Enter the list items separated by a space: ')
list = list(map(int, input().split()))

def Sum_Odd_Elements(list):

    print(list)
    sum = 0
    index = 0

    while index < len(list):
        if index % 2 != 0:
            sum += list[index]
        index += 1
    print(f'Sum = {sum}')

Sum_Odd_Elements(list)

