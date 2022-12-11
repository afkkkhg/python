"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""

class Hero():
    def __init__(self, hello, atack):
        self.hello = hello
        self.atack = atack

    def task (self):
        print('Привет', self.hello)
        print('Бой', self.atack)

class Magician(Hero):
    def hello(self):
        super().task()

    def atack(self):
        print('Ну')

Magician.hello()
Magician = Magician()
