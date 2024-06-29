#getter va setter = for next lesson
#encapsulation = callas ichidagi obyektlarni class ichida yaratish
#name magling
#private

# class Person:
#     def __init__(self, name, age):
        
#         self.__name = name
#         self.__age = age

# person = Person("John", 25)

# print(person.__name)
# # name magling

# # obj._ClassName_name
# print(person._Person__name)

# #getter va setter

class Person:
    def __init__(self, name, age):
        self._age = age
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        try:
            number = int(value)
            self._age = value
        except ValueError:
            print("Age must be a number")
person = Person('John', 30)
print(person.age)
person.age = 40
print(person.age)

