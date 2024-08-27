class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'Здравствуйте, меня зовут {self.name}.')

class Student(Person):
    def __init__(self, name, status = 'студент'):
        super().__init__(name)
        self.status = status

    def introduce(self):
        super().introduce()
        print(f"Я {self.status}.")

class Teacher(Person):
    def __init__(self, name, status = 'преподаватель'):
        super().__init__(name)
        self.status = status

    def introduce(self):
        super().introduce()
        print(f"Я {self.status}.")


student_1 = Student('Сергей Николаев')
student_1.introduce()

teacher_1 = Teacher('Зубков Иван Петрович')
teacher_1.introduce()



