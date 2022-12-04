
    # 3'. Задайте список из вещественных чисел. 
    # Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
    # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

def Difference_Min_Max(list):
    int_min = math.trunc(min(list))
    int_max = math.trunc(max(list))

    difference = (min(list) - int_min) - (max(list) - int_max)
    print(round(difference, 2))


list = [1.1, 1.2, 3.1, 5, 10.01]

Difference_Min_Max(list)