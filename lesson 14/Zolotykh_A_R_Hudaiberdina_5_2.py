class Employee:
    def __init__(self,age, name, salary):
        if age < 18:
            raise ValueError('Возраст работника не может быть меньше 18 лет')
        else:
            self._age = age
        self._name = name
        self._salary = salary

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError('Возраст работника не может быть меньше 18 лет')
        else:
            self._age = value
    @age.deleter
    def age(self):
        del self._age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_):
        self._name = name_
    @name.deleter
    def name(self):
        del self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary_):
        self._salary = salary_

    @salary.deleter
    def salary(self):
        del self._salary


