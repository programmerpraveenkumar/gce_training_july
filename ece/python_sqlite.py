import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect('mydata.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')

conn.commit()
conn.close()
