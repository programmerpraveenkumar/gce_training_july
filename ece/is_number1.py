# get the input
num = input("enter num 1")
num2 = input("enter num 2")
try:
        # chxeck input is number 
        if num.isnumeric() == False:
                raise("number1 is not number")
        elif num2.isnumeric() == False:
                raise("number2 is not number")
        else:
                res = int(num)+int(num2)
                # convert into string and print
                print(str(res))        
except Exception as e:
        print(e)