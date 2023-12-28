class User:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('Hello,'+ self.name + '!')


class Teacher(User):
    def get_salary(self):
        print('1000')


class Student(User):
    def get_grade(self):
        print('10')


teacher = Teacher('John')
student = Student('Mary')

teacher.greeting()
teacher.get_salary()

student.greeting()
student.get_grade()
