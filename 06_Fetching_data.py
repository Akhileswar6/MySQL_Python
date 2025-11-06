""" Fetching Data """

""" In order to select particular attribute columns from a table, we write the attribute names."""
# SELECT attr1, attr2 FROM table_name

""" In order to select all the attribute columns from a table, we use the asterisk ‘*’ symbol."""
# SELECT * FROM table_name

""" Example: Select data from MySQL table using Python"""

# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109",
  database = "akhildb"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
 
query = "SELECT Name, Branch FROM student1"
cursorObject.execute(query)
  
myresult = cursorObject.fetchall()
  
for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()