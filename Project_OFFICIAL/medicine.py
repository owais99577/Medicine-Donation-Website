import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

cur = conn.cursor()

conn.execute("create table useracc (name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, password TEXT UNIQUE NOT NULL, Number TEXT NOT NULL, age INTEGER NOT NULL, Address TEXT NOT NULL)")  
  
print("Table created successfully")  

conn.close()