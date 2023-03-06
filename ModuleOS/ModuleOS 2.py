"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""

import os

import os
name=0
os.mkdir("/Scrathes/python/Downloads/target")
for i in range(1, 11):
    name+=1
    os.mkdir("/Scrathes/python/Downloads/target/"+str(name))