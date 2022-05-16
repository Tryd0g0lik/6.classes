#Ул. Сибревкома 1

#Задача 1-2
class Mentor:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender

class Lecturer(Mentor):
  def __init__(self, name, surname, gender, courses):
    super().__init__(name, surname, gender)
    self.courses = courses

    self.courses_in_progress = []
    self.courses_attached = []
    self.grades = {}

class Student(Mentor):
  def __init__(self, name, surname, gender):
    super().__init__(name, surname, gender)
    self.finished_courses = []

    self.courses_in_progress = []
    self.courses_attached = []
    self.grades = {}
    self.mentors  = []

#Что мы
  def rate_lectur(self, lecturer, course, grade):

    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress:
    #if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress and lecturer.courses_in_progress in self.courses_attached:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'

class Reviewer(Mentor):
  def __init__(self, name, surname, gender, student, grade):
    super().__init__(name, surname, gender)

    self.student = student
    self.grade = grade
    self.courses_attached = []

  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_attached += ['Python']

#cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor = Reviewer('Klava', 'Pupkina', 'female', 'Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Frosya', 'surname', 'gender', 'courses')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_in_progress += ['Python']

best_student.rate_lectur(cool_lecturer, 'Python', 10)
best_student.rate_lectur(cool_lecturer, 'Python', 10)
best_student.rate_lectur(cool_lecturer, 'Python', 10)

print(best_student.grades)
print(cool_lecturer.grades)

# Везде вижу данный шаблон или его аналог
# 1) def __init__(self, name, surname, gender, student, grade):
#     super().__init__(name, surname, gender)
#
# Если в super заложить self, что получаем или что изменится во втором варианте?
# 2) def __init__(self, name, surname, gender, student, grade):
#     super().__init__(self.name, self.surname, self.gender)

#ЗАдача 2 онеь тяжело осваевается своей логико в отношении наследования. Нужны дополнительные задания для практики, с возможнойсть проверки. Есть такая возможность?