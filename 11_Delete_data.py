""" Delete Data from Table -> We can use the Delete query to delete data from the table in MySQL."""

# Example: Delete Data from MySQL table using Python

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
 
sql_query = "DELETE FROM students WHERE NAME = 'Rohit'"
cursorObject.execute(sql_query)

dataBase.commit()

print(f"✅ Record deleted successfully! Rows affected: {cursorObject.rowcount}")

# disconnecting from server
dataBase.close()