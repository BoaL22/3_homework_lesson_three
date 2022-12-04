
    # 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

    # - 45 -> 101101
    # - 3 -> 11
    # - 2 -> 10

def Bin_Number(num):
    bin = ''
    while num > 0:
        bin = str(num % 2) + bin
        num = num // 2
    print(f'  {bin}')

num = int(input())
print(bin(num))
Bin_Number(num)
