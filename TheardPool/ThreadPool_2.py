"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""
import
import queue
import concurrent.futures

def display_divisors(number):
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    print(f"Divisors of {number}: {divisors}")

number_queue = queue.Queue()
number_queue.put(10)
number_queue.put(20)
number_queue.put(30)
number_queue.put(40)

with concurrent.futures.ThreadPoo(max_workers=4) as executor:
    futures = [executor.submit(display_divisors, number_queue.get()) for _ in range(number_queue.qsize())]

    concurrent.futures.wait(futures)
