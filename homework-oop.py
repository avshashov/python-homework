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
        return sum_grade / counter_grades if counter_grades > 0 else 0.0

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


def avg_hm(students, subject):
    avg_grade = 0
    for student in students:
        avg_grade += sum(student.grades[subject])
    avg_grade /= len(students)
    return avg_grade


def avg_lecturers_grade(lecturers, subject):
    avg_grade = 0
    for lecturer in lecturers:
        avg_grade += sum(lecturer.lecturer_grades[subject])
    avg_grade /= len(lecturers)
    return avg_grade


student1 = Student('Harry', 'Potter', 'Male')
student2 = Student('Hermione', 'Granger', 'Female')
student1.add_finished_course('Git')
student1.courses_in_progress += ['SQL', 'Python']
student2.courses_in_progress += ['Git', 'Python']

mentor1 = Mentor('Rubeus', 'Hagrid')
mentor2 = Mentor('Remus', 'Lupin')

lecturer1 = Lecturer('Severus', 'Snape')
lecturer2 = Lecturer('Alastor', 'Moody')
lecturer1.courses_attached += ['SQL', 'Python', 'Git']
lecturer2.courses_attached += ['SQL', 'Python', 'Git']

reviewer1 = Reviewer('Albus', 'Dumbledore')
reviewer2 = Reviewer('Minerva', 'McGonagall')
reviewer1.courses_attached += ['SQL', 'Python', 'Git']
reviewer2.courses_attached += ['SQL', 'Python', 'Git']
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'SQL', 8)
reviewer2.rate_hw(student2, 'Git', 10)
reviewer2.rate_hw(student2, 'Python', 10)

student1.rate_lecturer(lecturer1, 'SQL', 7)
student1.rate_lecturer(lecturer1, 'Python', 6)
student2.rate_lecturer(lecturer2, 'Git', 3)
student2.rate_lecturer(lecturer2, 'Python', 8)

print(student1, student2, lecturer1, lecturer2, reviewer1, reviewer2, sep='\n\n', end='\n\n')
print(student1 > student2, lecturer1 > lecturer2)
print(avg_hm([student1, student2], 'Python'))
print(avg_lecturers_grade([lecturer1, lecturer2], 'Python'))
