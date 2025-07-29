from add import add,sub,mul
from  mymodule import checkNumber
from  mymodule2 import Person

result = add(4,5)
print(result)
result = mul(10, 3)
print(result)

try:
    checkNumber(150)
except Exception as e:
    print(e)

person = Person()
person.printName("sample")