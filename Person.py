#Python class Person with attributes: name and age of type string.
class Person():
    def __init__(self,n,a):
        self.name = n
        self.age = a
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self,n,a,s):
        Person.__init__(self,n,a)
        self.section=s
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Section: {self.section}")

student1=Student("Tom",30,"Computer Science")
student1.display()