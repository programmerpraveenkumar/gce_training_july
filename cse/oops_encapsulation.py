#class declaration
class Person:
    # constructor
    def __init__(self,name):
        self.name = name

        # set the name
    def setName(self,name):
            self.name = name

    # get the name
    def getName(self):
        return self.name

# create an instance of Person with param to __init
person = Person("some name")
person.setName("updated name")
person.getName()