"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""
class Utka():
    def Kr(self):
        print('кряяя')
    def Nos(self):
        print('носит шмот')
class Chelovek():
    def Kr(self):
        print('имитация кряяка')
    def Nos(self):
        print('носит настоящий шмот')

x1 = Utka()
x2 = Chelovek()
for i in (x1, x2):
    i.Kr()
    i.Nos()