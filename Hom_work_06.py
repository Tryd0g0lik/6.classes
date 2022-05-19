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
  def __init__(self, name, surname, gender, course):
    super().__init__(name, surname, gender)
    self.courses = course
    self.courses_in_progress = []
    self.courses_attached = []
    self.grades = {}


  def __str__(self):
    stud_name = self.name
    stud_surname = self.surname
    print(f'Имя: {stud_name}')
    print(f'Имя: {stud_surname}')
    return (stud_name, stud_surname)

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

  # def reviewer(self):
    
  def rate_lectur(self, lecturer, course, grade):

    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress:
      # if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress and lecturer.courses_in_progress in self.courses_attached:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
        return lecturer.grades
      else:
        lecturer.grades[course] = [grade]
      return lecturer.grades
    else:
      return 'Ошибка'
    self.grades_list = lecturer.grades

    #print ('111111',grades_list )

  def name_surname_student(self):
    name = self.name
    surname = self.surname
    # return [name, surname]
    return (name, surname)

  def __str__(self):
    name = self.name
    surname = self.surname

    return name, surname

class Reviewer(Student):

  # def __init__(self, name, surname, gender, student, grade ):
  def __init__(self, name, surname, gender):
    super().__init__(name, surname, gender)
    # self.student = student
    # self.student = ()
    # self.grade = grade
    # self.grade = {}
    # self.courses_attached = []

  def rate_hw(self, student, course, grade, status):

    # print('isinstance', isinstance(student, Student), Student.__init__().name)
    if status.strip().lower() == "student" or status.strip().lower() == "студент":
      # print('student', student)
      print('course', course)
      print('grades', student.grades)
      if course not in list(student.grades.keys()):

        print('1111', course)
        student.grades[course] = [grade]

        print('333', student.grades[course])
        # print(grades)
        return grade
      else:
        print('22', course)
        student.grades[course] += [grade] #student.grades[course].append(grade)
        print('444', student.grades)
        print(student.grades)
    else:
      return 'Ошибка'

class AverageGrades(Student):
  def __init__(self, grades):
    # Student.__init__(self, self.name, self.surname, self.gender)
    # Student().name
    self.grades = grades
    self.l_common_values = []
    self.l_common_key = []
    # self.name = name






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

  # def bal_name_subject(self, name_student, surname_student):
  def bal_name_subject(self):
    list_student_courses = []
    print()
    # super().__init__(self, name_student, surname_student)
    # super().__init__(self, name_student, surname_student)
    # Student.__init__(self.name, self.surname)
    # list_student_courses.append((name_student, surname_student))

    # print(self.name, 'self.name')
    # print(list_student_courses)
    # print(name_student)
    # print(surname_student)
    AverageGrades.grad(self, grades)
    # self.grades
    g = grades

    # if g != None: # and isinstance(name_student, Student):

    # print(g)



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

# class Student_grades(Reviewer, Lecturer):
  # def __init__(self, courses, student_grade):
    # student_grade = student_grade
    # student_course = courses
    #
#
#   def courses(self, courses, grade):
#     if self.courses != {} and isinstance(student, Student):
#       print(self.student_courses)
# print(Student_grades.mro())

# ЗАДАЧА 1-2
print('ЗАДАЧА 1-2')
# Студент
print("Введите Имя, Фамилия, Пол, Курс, Оценка - через запятую ',' ")
name, surname, gender, course, grade, status = 'petya', 'petrov', 'male', 'python', 4, 'student' #(input('Имя,
# Фамилия, Пол,  'Курс, Оценка: ')).strip().split(', ')

print("Reviewer!! Введите Имя, Фамилия, Пол - через запятую ',' ")
rev_name, rev_surname, rev_gender = 'Yasha', 'Kuznecove', 'male' #(input('Имя, Фамилия, Пол,
# Курс,  'Оценка: ')).strip().split(', ')

best_student = Student(name, surname, gender)
best_student.courses_in_progress += [course]
best_student.courses_attached += [course]

# student_corses = Student_grades.courses(course, grade)
# print('student_corses', student_corses)
# best_student.grades = {course : grade}
# petya, petrov, male, python, 4
# grades = {}
# grades['Git'] = [5]
# grades['Git'] += [10]
# grades['Git'] += [3]
# grades['Git'] += [1]
# grades['Git'] += [6]
# bal_student = AverageGrades(grade)
#print('55555', bal_student.grad(grades))
# average_bal = bal_student.grad(grades)

# Спец
# cool_reviewer = Reviewer('Klava', 'Pupkina', 'female')
cool_reviewer = Reviewer(rev_name, rev_surname, rev_gender)
cool_reviewer.rate_hw(best_student, course, grade, status)
cool_reviewer.courses_attached += ['Python']
#
# cool_reviewer.rate_hw(best_student, 'Python', 10)

# Лектор
# cool_lecturer = Lecturer('Frosya', 'surname', 'gender', 'courses')
# cool_lecturer.courses_attached += ['Python']
# cool_lecturer.courses_in_progress += ['Python']
# cool_lecturer.courses_attached += ['Pandas']
# cool_lecturer.courses_in_progress += ['Pandas']
#
# best_student.rate_lectur(cool_lecturer, 'Python', 10)
# best_student.rate_lectur(cool_lecturer, 'Python', 7)
# best_student.rate_lectur(cool_lecturer, 'Pandas', 10)

# print(best_student.grades)
# print(cool_lecturer.grades)

print(' ')

# ЗАДАЧА 3
print(' ЗАДАЧА 3')
# odj = Mentor('Dasha', 'Pupkina', 'male')
# print(odj.__str__())

print('')
# Средний бал лектору
print('Средний бал лектору')
# grades = {}
# fsd = Lecturer("name", "surname", "gender", "courses")
# grades['Python'] = [5]
# grades['Python'] += [10]
# grades['Python'] += [3]
# grades['Python'] += [1]
# grades['Python'] += [6]
# grades['Git'] = [7]

# bal_lector = AverageGrades(grades)
#print(AverageGrades(grades))
# fsd.__str__()
# print('Средний бал {}'.format(bal_lector.grad(grades)))

print('')
# Средний бал студента
print('Средний бал студентов ')
# name_student = (best_student.__str__())[0]
# surname_student = (best_student.__str__())[1]
# print('Имя: {}'.format(name_student))
# print('Фамилия: {}'.format(surname_student))
# print('Средняя оценка за домашние задания: {}'.format(average_bal))
# print('Курсы в процессе изучения: ', str(bal_student.cours()).strip("'][").replace("', '", ", "))
# print('Завершенные курсы: Введение в программирование')

print(' ')
# Возможность сравнивать между собой любой объект
print('Возможность сравнивать между собой лекторов')
# compere_lectos = compare(bal_lector.grad(grades), average_bal)
# compere_lectos.compare_result()
print('''Код раздут из-за ручной работы со словарем Не стал создавать  еще одну пару - лектора и студента. 
Класс "compare" позволяет сравнить любые 2 эллемента''')

print(' ')
# ЗАДАЧА 4
print('ЗАДАЧА 4')
#def bal_name_subject():
#print(grades)
# p = bal_student.bal_name_subject()
# print(best_student.name)

# name, surname, gender, course, grade
# names = []

def faculty_history(name, surname, course, grade, status = None, student = [], student_history = None, rev_name =
None, rev_gender = None, rev_lecturer = None, rev_surname = None):

  status = str(status).strip().lower()
  studend_meta_user = Student(name, surname, gender)
  student_meta = studend_meta_user.name_surname_student()
  student_grades = studend_meta_user.grades
  print(('student_meta: ', student_meta))

  # rewiewer_meta_user = Reviewer(rev_name, rev_surname, rev_gender, student, grade)
  rewiewer_meta_user = Reviewer(rev_name, rev_surname, rev_gender)
  # student_course_history = rewiewer_meta_user.rate_hw(studend_meta_user, course, grade)
  student_course_history = rewiewer_meta_user.rate_hw(student_meta, course, grade, status)

  if status == "student" or status == 'студент' and (name, surname) in student:
     (student_history[0])[student_meta] += student_course_history
     print('22', student_history)
     return student_history
  else:
    # s = Student(name, surname, gender)
    # student_meta = s.name_surname_student()
    print('33', student_meta)
    student = [{ student_meta : student_grades}]
    print('student', student)


faculty_history(name, surname, gender, course, grade, status)
# petya, petrov, male, python, 4, student
# Yasha, Kuznecove, male













# Везде вижу данный шаблон или его аналог
# 1) def __init__(self, name, surname, gender, student, grade):
#     super().__init__(name, surname, gender)
#
# Если в super заложить self, что получаем или что изменится во втором варианте?
# 2) def __init__(self, name, surname, gender, student, grade):
#     super().__init__(self.name, self.surname, self.gender)
