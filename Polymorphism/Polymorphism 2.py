"""
Создать базовый класс ОЛИМПИАДНЫЕ ЗАДАНИЯ (данные об участнике, количество тестовых примеров,
количество пройденных тестов).
Создать производные классы ЗАДАНИЯ «ВСЕ ИЛИ НИЧЕГО»
(задается максимальное количество баллов за задание (даются только когда все тесты пройдены)
и ЗАДАНИЯ «ЧЕМ БЫСТРЕЕ, ТЕМ ЛУЧШЕ» (задается время участника на решение,
лучшее время всех участников, максимальное количество баллов за задание,
процент снижения балла в минуту отставания от лучшего времени).
Для заданных примеров задач, которые решали участники,
упорядочить участников по росту набранных баллов и определить суммарное количество баллов,
набранных заданным участником олимпиады.
Для проверки использовать действия над списком,
в котором разместить объекты разных производных классов.
"""

class Task:
    def __init__(self, name, completed, max_score):
        self.name = name
        self.completed = completed
        self.max_score = max_score


class AllOrNothing(Task):
    def __init__(self, name, completed, max_score):
        super().__init__(name, completed, max_score)


class FasterIsBetter(Task):
    def __init__(self, name, completed, max_score, time_to_solve, score_for_task, percent, time_of_participant):
        super().__init__(name, completed, max_score)
        self.time_to_solve = time_to_solve
        self.score_for_task = score_for_task
        self.percent = percent
        self.time_of_participant = time_of_participant


class Participant:
    def __init__(self, name, tasks, total):
        self.name = name
        self.tasks = tasks
        self.total = total