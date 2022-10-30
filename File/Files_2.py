"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""

with open("texxt.txt", "r") as file:
    text1 = file.read()
with open("new.txt", "w") as file:
    file.write("но у меня не получается")
with open("new.txt", "r") as file:
    text2 = file.read()
with open("new.txt", "w") as file:
    file.write(text1 + text2)