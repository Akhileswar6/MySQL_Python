# Where Clause -> Where clause is used in MySQL database to filter the data as per the condition required. You can fetch, delete or update a particular set of data in MySQL database by using where clause.
# Example: Where clause in MySQL using Python

# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109",
  database = "gfg"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
 
query = "SELECT * FROM STUDENT where AGE >=20"
cursorObject.execute(query)
  
myresult = cursorObject.fetchall()
  
for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()