# Drop Tables
# Example 1: Drop Table in MySQL using Python
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
 
query ="DROP TABLE Student;"

cursorObject.execute(query)
dataBase.commit()

# disconnecting from server
dataBase.close()