""" Where Clause -> Where clause is used in MySQL database to filter the data as per the condition required.
You can fetch, delete or update a particular set of data in MySQL database by using where clause."""

# Example: Where clause in MySQL using Python

import mysql.connector
 
# Connect to the studentdb database 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109",
  database = "studentdb"
)

# Create a cursor object
cursorObject = dataBase.cursor()
 
sql_query = "SELECT * FROM students where marks >=90"
cursorObject.execute(sql_query)
  
myresult = cursorObject.fetchall()
  
print("🎓 Student Records:")
for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()