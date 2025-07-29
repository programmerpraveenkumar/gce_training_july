import mysql.connector

def update_user(user_id, new_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="user_db"
    )

    mycursor = mydb.cursor()
    sql = "UPDATE user1 SET name = %s WHERE id = %s"
    val = (new_name, user_id)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount, "record updated.")


id = input("Enter user ID to update: ")
name = input("Enter new name: ")   
update_user(1, "New Name")  


