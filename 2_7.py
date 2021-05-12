#1
class City:
    def __init__(self, name, population, language):
        self.name = name
        self.population = population
        self.language = language

    def say(self):
        print(f'name - {self.name}\npopulation - {self.population}\nlanguage - {self.language}\n')
        
a = City("Kyrgyzstan", 6000000, "kyrgyz")
a.say()


#2
class Monkey:

    max_age = 12
    loves_bananas = True

    def smth(self, max_age, loves_bananas):
        self.max_age = max_age
        self.loves_bananas = loves_bananas
    print(max_age, loves_bananas)

    def climb(self):
        print('I am climbing the tree') 
    

a = Monkey()
a.climb()

#3

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def calculate_age(self, year):
        print(f'Через {year} лет {self.name} исполнится {self.age + year}')

a = Person("John", 21, "male")
a.calculate_age(10)

#4

i dont know