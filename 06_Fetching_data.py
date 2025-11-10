""" Fetching Data """

""" In order to select particular attribute columns from a table, we write the attribute names."""
# SELECT attr1, attr2 FROM table_name

""" In order to select all the attribute columns from a table, we use the asterisk ‘*’ symbol."""
# SELECT * FROM table_name

""" Example: Select data from MySQL table using Python"""

import mysql.connector
 
# Connect to the StudentDB database 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109",
  database = "studentdb"
)

# Create a cursor object
cursorObject = dataBase.cursor()
 
# Execute the SQL query
sql_query = "SELECT student_id,name, branch FROM students"
cursorObject.execute(sql_query)
  
myresult = cursorObject.fetchall()
  
print("🎓 Student Records:") 
for row in myresult:
    print(row)

# disconnecting from server
dataBase.close()