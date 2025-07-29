import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="user_db"
)

mycursor = mydb.cursor()
mycursor.execute("select * from user1")
result = mycursor.fetchall()

for row in result:
    print(row)

mydb.commit()
mycursor.close()
mydb.close()
print(mycursor.rowcount, "record inserted.")


