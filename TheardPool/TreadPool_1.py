"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""

from queue import Queue
from threading import Thread
def familia(que):
    while True:
        familia=input()

        if familia=='off':
            break

        que.put(familia)


def kik(que):
    print(que.qsize())
    while True:
        try:
            name=que.get()
        except que.Empty:
            continue
        else:
            print(name, 'отчислен')
        que.task_done()


queue = Queue()
queue.put("pupkin")
t1=Thread(target=familia, args=(queue, ))
t1.start()
t2=Thread(target=kik, args=(queue, ), daemon=True)
t2.start()