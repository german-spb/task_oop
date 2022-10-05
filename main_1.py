class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def cf_grade(self):         # Метод подсчета средней оценки за ДЗ
        for value in self.grades.values():
            return round(sum(value)/len(value),1)
    def __str__(self):
        res = f'Имя студента: {self.name}\nФамилия студента: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.cf_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res
    def __gt__(self, other):    # Метод сравнения средней оценки у студентов
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.cf_grade() > other.cf_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    #grades = {}
    def cf_grade(self):
        for value in self.grades.values():
            return round(sum(value)/len(value),1)
    def __str__(self):
        res = f'Имя лектора: {self.name}\nФамилия лектора: {self.surname}\nСредняя оценка за лекцию: {self.cf_grade()}'
        return res
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.cf_grade() > other.cf_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя проверяющего: {self.name}\nФамилия проверяющего: {self.surname}'
        return res
#--------------------подсчет средней оценки за домашнее задание---------------
stud = {'Python': {'Зверев' : 4, 'Птицын' : 5, 'Сидоров' : 4}, 'Git' : {'Зверев' : 4, 'Птицын' : 3, 'Сидоров' : 3}}
def cf_grade_student(stud):
    for key, value in stud.items():
        i = []
        print('Средняя оценка по курсу ' + key)
        for value_1 in value.values():
             i.append(value_1)
        print(round(sum(i)/len(i),1))

#--------------------подсчет средней оценки за лекции ---------------------
lect = {'Вводдный курс': {'Конев' : 4, 'Мягкова' : 5, 'Епифанцев' : 5}, 'Git' : {'Конев' : 4, 'Мягкова' : 3, 'Епифанцев' : 4}}
def cf_grade_lecturer(lect):
    for key, value in lect.items():
        i = []
        print('Средняя оценка за лекцию ' + key)
        for value_1 in value.values():
             i.append(value_1)
        print(round(sum(i)/len(i),1))

student_1 = Student('Саша', 'Зверев', 'муж.')
student_1.courses_in_progress += ['Python','Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Иван', 'Птицын', 'муж.')
student_2.courses_in_progress += ['Python','Git']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Ларион', 'Конев')
lecturer_2 = Lecturer('Таисия', 'Мягкова')

reviewer_1 = Reviewer('Александр', 'Сазонов')
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2 = Reviewer('Петр', 'Николаев')
reviewer_2.courses_attached += ['Python', 'Git']

reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 9)

student_1.rate_lect(lecturer_1, 'Python', 8)
student_1.rate_lect(lecturer_2, 'Python', 5)
student_2.rate_lect(lecturer_1, 'Python', 3)
student_2.rate_lect(lecturer_2, 'Python', 4)

print(lecturer_1)
print(lecturer_2)
print((lecturer_1 > lecturer_2))
print(reviewer_1)
print(reviewer_2)
print(student_1)
print(student_2)
print((student_1 > student_2))
print('Посчет средних оценок:')
cf_grade_student(stud)
cf_grade_lecturer(lect)