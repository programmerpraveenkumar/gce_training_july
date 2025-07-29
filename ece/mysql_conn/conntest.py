import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="user_db"
)
print("Connected database successfully.")