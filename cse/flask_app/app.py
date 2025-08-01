from flask import Flask,jsonify,request,render_template
from flask_mysqldb import MySQL

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_database_name'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/myname/<name>')
def hello_world(name):
    return jsonify({"name" : name})

@app.route('/myhtml')
def myHtml():
    return render_template("home.html")

@app.route('/user_detail')
def userDetail():
    id = request.args.get("id")
    sql = f"SELECT * FROM users where id = {id}"
    cur = mysql.connection.cursor()
    cur.execute(sql)  
    results = cur.fetchall() 
    print(results)
    cur.close()

    return render_template("user_detail.html",
                           id=results[0][0],
                           name=results[0][1],
                           email=results[0][2],
                           password = results[0][3]
                           )

@app.route('/getData')
def getData():
    id = request.args.get("id")
    sql = ""
    if id is None:
        sql = "SELECT * FROM users"
    else:
        sql = f"SELECT * FROM users where id = {id}"

    cur = mysql.connection.cursor()
    cur.execute(sql)  
    results = cur.fetchall() 
    cur.close()
    return jsonify(results)

@app.route('/getDataInHtml')
def getDataInHtml():
    id = request.args.get("id")
    sql = ""
    if id is None:
        sql = "SELECT * FROM users"
    else:
        sql = f"SELECT * FROM users where id = {id}"

    cur = mysql.connection.cursor()
    cur.execute(sql)  
    results = cur.fetchall() 
    cur.close()
    return render_template("userlist.html",userlist=results)






# @app.route('/register_save',methods=["GET","post"])
# def register_save():
# 	if request.method == "GET":
#     	return render_template("register.html")
#     else:
#         id = request.form['id']
#         email = request.form['email']
#         password = request.form['password']

#         cur = mysql.connection.cursor()
#         sql ="insert into users(id,email,password) values(%s,%s,%s)"
#         val = [id,email,password]
#         cur.execute(sql,val)  
#         mysql.connection.commit()
        
#         cur.close()
#         return "register success"


if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()