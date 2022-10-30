"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.
Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""


def calculate(*args):
    if len(args) <= 0:
        exit()
    summa = 0
    for i in args:
        summa += i
    middle = summa / len(args)
    higher_than_mid = []
    for j in args:
        if j > middle:
            higher_than_mid.append(j)
    return middle, tuple(higher_than_mid)