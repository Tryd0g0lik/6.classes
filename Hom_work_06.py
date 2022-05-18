# Ул. Сибревкома 1

# Задача 1-2
class Mentor:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender

  def __str__(self):
    print('Имя: {}'.format(self.name))
    print('Фамилия: {}'.format(self.surname))



class Lecturer(Mentor):
  def __init__(self, name, surname, gender, courses):
    super().__init__(name, surname, gender)
    self.courses = courses
    self.courses_in_progress = []
    self.courses_attached = []
    self.grades = {}


  def __str__(self):

    print(f'Имя: {self.name}')
    print(f'Имя: {self.surname}')


class AverageGrades():
  def __init__(self, grades):
    self.grades = grades

  def grad(self, grades):
    new_l = 0
    new_l = []

    grades[list(grades.keys())[0]] += list(grades.values())[0]

    l = list(grades.values())
    l_len = len(l)
    for i in range(l_len):
      new_l = new_l + l[i]

    grades_average_sum = sum(new_l)
    grades_average_len = len(new_l)
    aver = round(grades_average_sum / grades_average_len, 2)

    return aver

class Student(Lecturer):
  def __init__(self, name, surname, gender):
    Mentor.__init__(self, name, surname, gender)
    self.finished_courses = []

    self.courses = ''
    self.courses_in_progress = []
    self.courses_attached = []
    self.grades = {}
    self.mentors = []

  def rate_lectur(self, lecturer, course, grade):

    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress:
      # if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress and lecturer.courses_in_progress in self.courses_attached:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]

      else:
        lecturer.grades[course] = [grade]

    else:
      return 'Ошибка'

    #return ('111111', lecturer.grades)
# class StudentGrade():
#   def __init__(self, student, course, grade, name, surname, gender):
#     Mentor.__init__(name, surname, gender)
#     self.student = student
#     self.course = course
#     self.grade = grade
#


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
        #print('333', student.grades)
      else:
        student.grades[course] = [grade]
        #print('444', student.grades)
    else:
      return 'Ошибка'

# ЗАДАЧА 1-2
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_attached += ['Python']

# cool_mentor = Reviewer('Some', 'Buddy')
cool_reviewer = Reviewer('Klava', 'Pupkina', 'female', 'Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Frosya', 'surname', 'gender', 'courses')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_in_progress += ['Python']
cool_lecturer.courses_attached += ['Pandas']
cool_lecturer.courses_in_progress += ['Pandas']

best_student.rate_lectur(cool_lecturer, 'Python', 10)
best_student.rate_lectur(cool_lecturer, 'Pandas', 10)

print(best_student.grades)
print(cool_lecturer.grades)
print(' ')

# ЗАДАЧА 3
print(' ЗАДАЧА 3')
odj = Mentor('Dasha', 'Pupkina', 'male')
print(odj.__str__())

print('')


# Средний бал лектору
print('Средний бал лектору')
grades = {}
print('')
fsd = Lecturer("name", "surname", "gender", "courses")
grades['courses'] = [5]
grades['courses'] += [10]
grades['courses'] += [3]
grades['courses'] += [1]
grades['courses'] += [6]

fsd = Lecturer("name", "surname", "gender", "courses")
grades['coooouprses'] = [7]

bal = AverageGrades(grades)
fsd.__str__()
print('Средний бал {}'.format(bal.grad(grades)))

print('')
# Средний бал студентов
print('Средний бал студентов ')



# def StudentGrade():
#   Mentor.__init__(name, surname, gender)
#   self.student = student
#   self.course = course
#   self.grade = grade
# StudentGrade();
# Везде вижу данный шаблон или его аналог
# 1) def __init__(self, name, surname, gender, student, grade):
#     super().__init__(name, surname, gender)
#
# Если в super заложить self, что получаем или что изменится во втором варианте?
# 2) def __init__(self, name, surname, gender, student, grade):
#     super().__init__(self.name, self.surname, self.gender)
