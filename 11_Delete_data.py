""" Delete Data from Table -> We can use the Delete query to delete data from the table in MySQL."""

# Example: Delete Data from MySQL table using Python

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
 
query = "DELETE FROM student1 WHERE NAME = 'Nikhil'"
cursorObject.execute(query)
dataBase.commit()

# disconnecting from server
dataBase.close()