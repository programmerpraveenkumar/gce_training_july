import mysql.connector

def check_email_exists(email):
     
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="user_db"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(id) as count FROM user1 where email = %s", (email,))
    myresult = mycursor.fetchall()
    print(myresult)
    if myresult[0][0] >=1 :
        print("Email already exists")
    else:
        print("Email does not exist")   

    mycursor.close()
    mydb.close()    
# print(myresult[0][0])

input_email = input("Enter the email to check: ")
check_email_exists(input_email)