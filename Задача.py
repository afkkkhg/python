class Worker:
    def __init__(self, name: str, position: str, experience: int):
        self.name = name
        self.position = position
        self.experience = experience

    def print_info(self):
        if int(self.experience) < 2:
            print('Имя: {}, Должность: {},  Стаж: {} год'.format(self.name, self.position, self.experience))
        elif 1 < int(self.experience) < 5:
            print('Имя: {}, Должность: {},  Стаж: {} года'.format(self.name, self.position, self.experience))
        else:
            print('Имя: {}, Должность: {},  Стаж: {} лет'.format(self.name, self.position, self.experience))


worker = Worker('Василий', 'Системный администратор', 3)
worker.print_info()