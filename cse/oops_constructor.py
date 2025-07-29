#class declaration
class Person:
    # constructor
    def __init__(self,name):
        self.name = name

    # print a message
    def printName(self):
        print(self.name)

# create an instance of Person with param to __init
person = Person("some name")
person.printName()