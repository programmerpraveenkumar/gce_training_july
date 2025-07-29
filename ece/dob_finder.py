from datetime import date

def ageFinder(dob):
    dateObj = dob.split('-')
    year = int(dateObj[2])
    month = int(dateObj[1])
    day = int(dateObj[0])
    today = date.today()
    birthdate = date(year, month, day)
    age = today.year - birthdate.year
    return age

dob = input("enter the dob in dd-m-yyyy")
age = ageFinder(dob)
print(age)
