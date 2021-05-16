# class Cube:

#     width = 50

#     def __init__(self, length, weight):
#         self.length =  length
#         self.weight = weight
#         print(self.length, self.height)

#     def show_length(self):
#         print(f'my length is {self.length}')

# l = Cube(50, 40)
# s = Cube(100, 60)

# l.show_length()
# s.show_length()


# class Cube:

#     width = 50



#     def addition(self, *args):
#         return sum(args) + self.width

# class Car:

#     width = 50

#     # создаем атрибуты класса
#     name = "c200"
#     make = "mercedez"
#     model = 2008

#     # создаем методы класса
#     def start(self):
#         print ("Заводим двигатель")

#     def stop(self):
#         print ("Отключаем двигатель")
    
#     def additional(self, *args):
#         return sum(args) + self.width
        


# # Создаем объект класса Car под названием car_a
# car_a = Car()
 
# # Создаем объект класса Car под названием car_b
# car_b = Car()
# print(car_b.additional(1, 12))


# class Telephone:


#     name = 'Iphone'
#     color = 'Gold'
#     price = '300000'

#     def __init__(self, asd, gg):
#         self.asd = asd
#         self.gg = gg

#     def addition(self):
#         print(self.asd + self.gg)

# a = Telephone(121, 323)
# a.addition()


# class Animal:

#     amount: 100
#     name: "Tiger"
#     color: "orange"


#     def __init__(self, asd, qwer):
#         self.asd = asd
#         self.qwer = qwer

#     def addition(self):
#         print(self.asd + self.qwer)

# a = Animal(2323, 323)
# a.addition()


# class SchoolMember:
#     '''Представляет любого человека в школе.'''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('(Создан SchoolMember: {0})'.format(self.name))
#     def tell(self):
#         '''Вывести информацию.'''
#         print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

# class Teacher(SchoolMember):
#     '''Представляет преподавателя.'''
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print('(Создан Teacher: {0})'.format(self.name))

#     def tell(self):
#         SchoolMember.tell(self)
#         print('Зарплата: "{0:d}"'.format(self.salary))

# class Student(SchoolMember):
#     '''Представляет студента.'''
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('(Создан Student: {0})'.format(self.name))

#     def tell(self):
#         SchoolMember.tell(self)
#         print('Оценки: "{0:d}"'.format(self.marks))

# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)

# print() # печатает пустую строку

# members = [t, s]
# for member in members:
#     member.tell() # работает как для преподавателя, так и для студента


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Wild_animals:
#     def forest(self):
#         print("I am wild animal")


# class Pet_animals:
#     def house(self):
#         print("I am pet animal")


# class Pig(Wild_animals, Pet_animals):
#     pass

# a = Pig()
# a.forest()
# a.house()


class Transport:
    def __init__(self, point_a, point_b):
    
        self.point_a = point_a
        self.point_b = point_b
        
    def travel(self):
        print(f'Going from point {self.point_a} to {self.point_b}')s


class Car(Transport):
    def travel(self):
        super().travel()
        print("travelling by road")

class Plane(Transport):
    def travel(self):
        super().travel()
        print("travelling by air")

class Boat(Transport):
    def travel(self):
        super().travel()
        print("travelling by water")

class Motorcycle(Car):
    def travel(self):
        super().travel()
        print("very fast")

a = Motorcycle('Issyk-Kol', 'Bishkek')
a.travel()