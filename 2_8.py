#1
class House:
    def __init__(self, street, color, number):
        self.street = street
        self.color = color
        self.number = number

    def show_info(self):
        print(f'Street is - {self.street}\ncolor is - {self.color}\nnumber is - {self.number}')

a = House("Abaya 40", "White", "79")
b = House("Politeh", "Red", "132")
a.show_info()
print("==============")
b.show_info()

#2
class Human:
    def _init_(self, name, age, favorite_lesson):
        self.name = name
        self.age = age
        self.favorite_lesson = favorite_lesson


class Teacher(Human):
    def _init_(self, name, age, favorite_lesson, specialty, salary):
        super()._init_(name, age, favorite_lesson)
        self.specialty = specialty
        self.salary = salary


class Student(Human):
    def _init_(self, name, age, favorite_lesson, grade):
        super()._init_(name, age, favorite_lesson)
        self.grade = grade

h = Human("Elya", 18, "English")
t = Teacher("Sam", 45, "History", 50000, "Art")
s = Student("Dan", 16, 100, "Phesical Training")





#3

class School:
    def wear_uniform(self):
        print("В школе все должны носить форму")

class University:
    def wear_uniform(self):
        print("Можно носить любую одежду, если ты студент")

a = School()
b = University()
a.wear_uniform()
b.wear_uniform()

#4
class Human:
    def eat_spaghetti(self):
        print("Я могу есть спагетти")

class Robot:
    def drink_oil(self):
        print("Я могу потреблять машинное масло")

class Cyborg(Human, Robot):
    pass

a = Cyborg()
a.eat_spaghetti()
a.drink_oil()

