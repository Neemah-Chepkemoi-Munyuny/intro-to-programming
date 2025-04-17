import sqlite3 as sl

con = s1.connect('test.db')

print ("Connected to test.db successfully")

conn.execute("""
   CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       age INTEGER NOT NULL
             );

""")
 
sql = "INSERT INTO users (id,name, age) VALUES (?, ?)"

data = [
    (1, 'John', 25),
    (2, 'Jane', 30),
    (3, 'Alice', 28),
    (4, 'Bob', 35), ]

with conn.executemany(sql, data) 

data = conn.execute("SELECT * FROM USER WHERE age > 26")

for row in data:
    print(row)
