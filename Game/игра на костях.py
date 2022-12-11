import random

stop = False
while True:
    stop = input('1 игрок бросает кубик. Нажмите Enter для броска. (s + enter, чтобы закончить)')
    if stop:
        break
    first_count = random.randint(2, 7) - 1
    print(f'выпало число {first_count}')
    input('2 игрок бросает кубик. Нажмите Enter для броска.')
    second_count = random.randint(2, 7) - 1
    print(f'выпало число {second_count}')
    if first_count > second_count:
        print('Игрок один победил')
    elif first_count < second_count:
        print('Игрок два победил')
    else:
        print('Ничья')
