num = input("Enter a number: ")

# raise an exception if the input is not a number
try:
    if not num.isnumeric():
        raise ValueError("Input is not a valid number.")
    else:
        print(num)    

except ValueError as e:
    print(e)