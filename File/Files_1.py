"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""

m = open('test.txt', 'w')
with open('test.txt', 'w') as d:
    d.write("я гений и стараюсь учить питон")
with open('test.txt', 'r') as a:
    x = a.read(7)
    print(x)