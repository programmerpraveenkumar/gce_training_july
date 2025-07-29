#class declaration
class Calculator:
    # constructor
    def __init__(self):
        print("this init")
        
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def action(self,action,a,b):
        if(action == 'add'):
            return self.add(a,b)
        if(action == 'sub'):
            return self.sub(a,b)
            # TODO for mul and div


calc = Calculator()

action = input("Enter the action")
num1 = input("Enter the number1")
num2 = input("Enter the number2")
result = calc.action(action,int(num1),int(num2))
print(result)