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

class Student(Lecturer):
  def __init__(self, name, surname, gender):
    Mentor.__init__(self, name, surname, gender)
    self.name = name
    self.surname = surname

    self.finished_courses = []

    self.courses = ''
    self.courses_in_progress = []
    self.courses_attached = []
    self.grades = {}
    self.mentors = []
    self.grades_list = []


  def rate_lectur(self, lecturer, course, grade):

    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress:
      # if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress and lecturer.courses_in_progress in self.courses_attached:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]

      else:
        lecturer.grades[course] = [grade]
      return lecturer.grades
    else:
      return 'Ошибка'
    self.grades_list = lecturer.grades

    #print ('111111',grades_list )

  def __str__(self):

    meta_list_student = [self.name, self.surname]
    return meta_list_student

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

class AverageGrades():
  def __init__(self, grades):
    self.grades = grades
    self.l_common_values = []
    self.l_common_key = []

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
    #print('888', grades)
    return aver

  def cours(self):
    listcours = list(grades.keys())
    return listcours

  def bal_name_subject(self):
    # print('777', Student.__str__(self))
    AverageGrades.grad(self, grades)
    # self.grades
    g = grades

    if g != None:
      print(g)



class compare():
  def __init__(self, element1, element2):
    self.element1 = element1
    self.element2 = element2

  def compare_result(self):
    element1 = self.element1
    element2 = self.element2

    if element1 < element2:
      print('Сравнение: {} < {}'.format(element1, element2) )
    elif element1 > element2:
      print('Сравнение: {} > {}'.format(element1, element2) )
    else:
      print('Сравнение: {} = {}'.format(element1, element2) )


# ЗАДАЧА 1-2
# Студент
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_attached += ['Python']
grades = {}
grades['Git'] = [5]
grades['Git'] += [10]
grades['Git'] += [3]
grades['Git'] += [1]
grades['Git'] += [6]
bal_student = AverageGrades(grades)
#print('55555', bal_student.grad(grades))
average_bal = bal_student.grad(grades)

# Спец
cool_reviewer = Reviewer('Klava', 'Pupkina', 'female', 'Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)

# Лектор
cool_lecturer = Lecturer('Frosya', 'surname', 'gender', 'courses')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_in_progress += ['Python']
cool_lecturer.courses_attached += ['Pandas']
cool_lecturer.courses_in_progress += ['Pandas']

best_student.rate_lectur(cool_lecturer, 'Python', 10)
best_student.rate_lectur(cool_lecturer, 'Python', 7)
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
fsd = Lecturer("name", "surname", "gender", "courses")
grades['Python'] = [5]
grades['Python'] += [10]
grades['Python'] += [3]
grades['Python'] += [1]
grades['Python'] += [6]
grades['Git'] = [7]

bal_lector = AverageGrades(grades)
#print(AverageGrades(grades))
fsd.__str__()
print('Средний бал {}'.format(bal_lector.grad(grades)))

print('')
# Средний бал студента
print('Средний бал студентов ')
name_student = (best_student.__str__())[0]
surname_student = (best_student.__str__())[1]
print('Имя: {}'.format(name_student))
print('Фамилия: {}'.format(surname_student))
print('Средняя оценка за домашние задания: {}'.format(average_bal))
print('Курсы в процессе изучения: ', str(bal_student.cours()).strip("'][").replace("', '", ", "))
print('Завершенные курсы: Введение в программирование')

print(' ')
# Возможность сравнивать между собой любой объект
print('Возможность сравнивать между собой лекторов')
compere_lectos = compare(bal_lector.grad(grades), average_bal)
compere_lectos.compare_result()
print('''Код раздут из-за ручной работы со словарем Не стал создавать  еще одну пару - лектора и студента. 
Класс "compare" позволяет сравнить любые 2 эллемента''')

print(' ')
# ЗАДАЧА 4
print('ЗАДАЧА 4')
#def bal_name_subject():
#print(grades)
p = bal_student.bal_name_subject()
print(p)














# Везде вижу данный шаблон или его аналог
# 1) def __init__(self, name, surname, gender, student, grade):
#     super().__init__(name, surname, gender)
#
# Если в super заложить self, что получаем или что изменится во втором варианте?
# 2) def __init__(self, name, surname, gender, student, grade):
#     super().__init__(self.name, self.surname, self.gender)
