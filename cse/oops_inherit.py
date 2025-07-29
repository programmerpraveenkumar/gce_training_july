
class Person():
    cityName = "mumbai"
    def printName(self,name):
        print(name)
   
class Ashok(Person):
    def printDetails(self):
        print("some message")

class Arun(Person):
    def printDetails(self):
        print("some message")

obj = Ashok()
obj.cityName = "new city"
obj.printName("ashok")

obj1 = Arun()
obj1.cityName = "london"
obj1.printName("arun")
