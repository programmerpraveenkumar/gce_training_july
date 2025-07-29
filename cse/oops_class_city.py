#class declaration
class City:
    def addCityDetails(self,name,country):
        self.name = name
        self.country = country

    def printCityDetails(self):
        print("City Name: " + self.name)
        print("Country: " + self.country)
      

#object or instance creation
delhi = City()
# calling the method
delhi.addCityDetails("delhi", "India")
delhi.printCityDetails()
print(delhi.name)

mumbai = City()
# calling the method
mumbai.addCityDetails("mumbai", "India")
mumbai.addCityDetails("London", "India")
mumbai.printCityDetails()