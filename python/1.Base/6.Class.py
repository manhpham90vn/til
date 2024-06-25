class Person:
    x = 1

manh = Person()
print(manh.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"

manh = Person("Manh", 25)
print(manh.name)
print(manh.age)
print(manh)

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old and graduated in {self.graduationyear}"
    
    def welcome(self):
        print(f"Welcome {self.name} to the class of {self.graduationyear}")

manh = Student("Manh", 25, 2021)
print(manh.name)
print(manh.age)
print(manh.graduationyear)    
manh.welcome()