try:
        num = int(input("enter number"))

        if num > 100:
                raise TypeError("number is `greater than 100")
                # raise  "number is `greater than 100"

        else:
                print("ok...")
except Exception as e:
	print(e)