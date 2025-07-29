import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect('mydata.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

conn.commit()
conn.close()
