def is_valid(num):
    if num.isdigit() and 0 < int(num) and float(num) == int(num):
        return True
    else:
        return False

print('\nДобро пожаловать в числовую угадайку')

while True:

    n = 100

    print('\nХотите воспользоваться возможностью указать правую границу числового промежутка? (да/нет)\n')
    ans = input()
    if ans == 'да':
        print('\nЯ загадаю число от 1 до (введите любое целое положительное число):')
        n = int(input())
    print()
    
    print('Я загадал, время угадывать!\n')

    from random import randrange
    rand_num = randrange(1, n + 1)

    count = 0

    while True:
        num = input()
        if is_valid(num):
            num = int(num)
            if num == rand_num:
                print('\nВы угадали, поздравляем!')
                break
            elif num < rand_num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif num > rand_num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        else:
            print('А может быть все-таки введем целое положительное число?')

    print('\nВы угадали за', count + 1, 'попыток')
    print()
    print('Хотите угадать еще одно число? (да/нет)\n')
    ans = input()
    if ans == 'нет':
        print('\nДо новых встреч!\n')
        break

