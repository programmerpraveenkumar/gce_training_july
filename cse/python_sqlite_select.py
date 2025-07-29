import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect('mydata.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
