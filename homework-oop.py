class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_course(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in \
                lecturer.courses_attached:
            lecturer.lecturer_grades.setdefault(course, []).append(grade)
        else:
            print('Ошибка')

    def __avg_grade(self):
        sum_grade, counter_grades = 0, 0
        for grade in self.grades.values():
            sum_grade += sum(grade)
            counter_grades += len(grade)
        return sum_grade / counter_grades

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: ' \
               f'{self.__avg_grade()} \nКурсы в процессе изучения: {courses_in_progress} \nЗавершенные курсы: ' \
               f'{finished_courses}'

    def __lt__(self, other):
        return self.__avg_grade() < other.__avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def __avg_grade(self):
        sum_grade, counter_grades = 0, 0
        for grade in self.lecturer_grades.values():
            sum_grade += sum(grade)
            counter_grades += len(grade)
        return sum_grade / counter_grades

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.__avg_grade()}'

    def __lt__(self, other):
        return self.__avg_grade() < other.__avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            student.grades.setdefault(course, []).append(grade)
        else:
            print('Ошибка')

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'



