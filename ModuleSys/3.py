"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""

import sys
my_file=open(str(sys.argv[2]), ' p+')
my_file.write(str(sys.argv[1]))
