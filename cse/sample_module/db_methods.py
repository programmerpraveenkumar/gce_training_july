from db_config import getDb

def inserData(id,name,email):
    mydb = getDb()
    mycursor = mydb.cursor()
    sql = "INSERT INTO user1 (id,name, email)VALUES (%s,%s,%s)"
    val = [id, name, email]
    mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()
    mydb.close()
    print("data is inserted")



# def updateData():

def deleteData():
    mydb =  getDb()
    mycursor = mydb.cursor()
    sql = "delete from user1 where id = %s"
    val = [id]
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("data is deleted")


def SelectData():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="user_db"
    )
    mycursor = mydb.cursor()
    sql = "select * from user1"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return result

