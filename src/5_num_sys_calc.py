from re import I


def binary_to_decimal(num):
    res = 0
    n = int(num)
    for i in range(len(num)):
        res += (n%10)*(2**i)
        n //= 10

    return res

def octal_to_decimal(num):
    res = 0
    n = int(num)
    for i in range(len(num)):
        res += (n%10)*(8**i)
        n //= 10

    return res

def hexadecimal_to_decimal(num):
    res = 0
    num = [c for c in num]
    n = []
    for i in range(len(num)):
        switcher = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
        'F': 15}
        if num[i] in "ABCDEF":
            n.append(switcher.get(num[i]))
        if num[i] in "1234567890":
            n.append(int(num[i]))

    for i in range(len(n)):
        res += n[len(n) - 1 - i]*(16**i)
    return res

def decimal_to_something(num, radix):
    res = ''
    num = int(num)
    while num >= radix - 1:
        tmp = num % radix
        if tmp > 9:
            switcher = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            tmp = switcher.get(tmp)
        else:
            tmp = chr(tmp + 48)
        res = tmp + res
        num //= radix

    return res

print("Что вы хотите сделать?")
print("1. Перевести из десятичной системы счисления в любую другую")
print("2. Перевести из какой-либо системы счиления в десятичную")
choise = int(input())
if choise == 1:
    num = input("Введите число: ")
    radix = int(input('Введите основание той системы счисления, в которую вы хотите его перевести: '))
    num = decimal_to_something(num, radix)
elif choise == 2:
    radix = int(input('Введите основание той системы счисления, из которой вы переводите число: '))
    num = input('Введите число: ')
    if radix == 2:
        num = binary_to_decimal(num)
    elif radix == 8:
        num = octal_to_decimal(num)
    elif radix == 16:
        num = hexadecimal_to_decimal(num)
    else:
        print("Неверный ввод, попробуйте еще раз")
else:
    print("Неверный ввод, попробуйте еще раз")

if num:
    print(num)
