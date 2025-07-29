list = ["one","two","three"]
print(list[0])
try:
    # below line will throw the error
    print(list[5])
except Exception as e:
        print("error in array")

print("this is the last line")