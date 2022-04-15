from random import choice

def print_ans():
    answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 
                'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 
                'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 
                'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 
                'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    print('****', choice(answers), '****\n')

def greeting():
    print('\nПривет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    print('\nРазрешите узнать ваше имя?\n')
    name = input()
    print('\nПриветсвую,', name, end='. ')

def is_exit():
    print('Хотите ли вы задать еще вопрос? (да/нет)\n')
    while True:
        ans = input()
        if ans == 'нет':
            print('\nВозвращайтесь, если возникнут вопросы!\n')
            return True
        elif ans == 'да':
            print()
            return False
        else:
            print('Я вас не понимаю, попробуйте еще раз\n')

def egine():
    while True:
       print('Задайте свой вопрос и нажмите на клавишу enter.')
       tmp = input()
       print_ans()
       if is_exit():
           break

greeting()
egine()

