"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""

class Hero:
    def __init__(self, health, power, rank):
        self.health = health
        self.power = power
        self.__rank = rank

    def sett_rank(self, rank):
        self.__rank = rank

    def gett_rank(self):
        return self.__rank

    def dell_rank(self):
        del self.__rank

    def fightt(self, enemy):
        while self.power > 0:
            enemy.health -= 5
            self.power -= 15
        if enemy.health < 0:
            self.sett_rank('победитель')
            print(self.gett_rank())
        else:
            self.dell_rank()
            print('лузер')


def main():
    hero1 = Hero(20, 100, ' - 1')
    hero2 = Hero(20, 200, ' - 0')
    hero1.fightt(hero2)


main()