def main(input):
    if 'распи' in input.lower(): # обращемся к тайм функции
        timetable()
    if 'трени' in input.lower():
        socks()
    if 'оплата' in input.lower():
        sick()
    if 'назва' in input.lower():
        mash()
    if 'сайт' in input.lower():
        slime()


def timetable():
    print('Часы работы спорткомплекс Пн - с 8:00 до 22:00 Ср - 8:00 до 22:00 Пт - 8:00 до 22:00')
    print('Вы хотите посетить тренировку? Введите - да/нет')
    t1=input()
    s1={}
    if t1=='да':
        print('Выберите день недели')
        t2=input()
        print('Введите удобное время с 8:00 до 22:00')
        t3=int(input())
        if 8<=t3<=22:
            s1[t2]=t3 # т2 ключ словаря , а т3 значение
            print('Вы записались на', s1)
def socks():
    print('Славной тренировки!')
def sick():
    print('К оплате за месяц - 7000')
def mash():
    print('ООО СЛАВНО г.Сочи, пр.Рекордов, д.15')
def slime():
    print('https://tools.dlink.com/wifiplanner/Portaldlink?RAS=BpbDIWfwLSmPsHKVY7K+8rLdwGmDRvEWd4+4tk3ppcw=&FM=46OwnJbhXPQWRkPLXlikuA==')