import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase",
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")

sqltable = """CREATE TABLE IF NOT EXISTS user(
         id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
         name VARCHAR(255),
         age INT,
         address VARCHAR(255)    
)"""
mycursor.execute(sqltable)      
#sql = 'SHOW TABLES'

sqlinsert = "INSERT INTO user (name, age, address) VALUES (%s, %s, %s)"

data = [
    ('John', 25, 'New York'),
    ('Jane', 30, 'Los Angeles'),
    ('Mike', 35, 'Chicago'),
    ('Sara', 28, 'Houston'),
    ('Tom', 40, 'Phoenix')
]

mycursor.executemany(sqlinsert, data)

mydb.commit()

sqlusers="SELECT * FROM user"

mycursor.execute(sqlusers)

myresult = mycursor.fetchall()

for user in myresult:
    print(user)