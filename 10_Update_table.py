""" Update Data -> The update query is used to change the existing values in a database.
By using update a specific value can be corrected or updated. It only affects the data and not the structure of the table.
The basic advantage provided by this command is that it keeps the table accurate."""

# Example: Update query in MySQL using Python

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
 
sql_query = "UPDATE students SET marks = 96 WHERE Name ='Akhileswar'"
cursorObject.execute(sql_query)

dataBase.commit()

print(f"✅ Record updated successfully! Rows affected: {cursorObject.rowcount}")

# disconnecting from server
dataBase.close()