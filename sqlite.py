#This Python script demonstrates basic SQLite operations using the sqlite3 module, including how to create a database, define a table, insert #records, and query data. Here's a breakdown of what the code does:


import sqlite3

## connect to sqlite
connection = sqlite3.connect('student.db')

## create a cursor object t0 insert record, create table, 
cursor  = connection.cursor()

# create the table

table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

##insert some more records
cursor.execute('''Insert into STUDENT values('Soham', 'AI/ML', 'A', 90)''')
cursor.execute('''Insert into STUDENT values('Parth', 'Data Science', 'A', 95)''')
cursor.execute('''Insert into STUDENT values('Sankalp', 'Full Stack', 'B', 82)''')
cursor.execute('''Insert into STUDENT values('Nitin', 'Full Stack', 'A', 89)''')
cursor.execute('''Insert into STUDENT values('Arnav', 'MLOPS', 'B', 88)''')
cursor.execute('''Insert into STUDENT values('Naman', 'Cloud Computing', 'B', 81)''')

## display records
print("Inserted records are: ")
data = cursor.execute(''' Select * From STUDENT''')
for row in data:
    print(row)


#commit changes in the databases
connection.commit()
connection.close()




