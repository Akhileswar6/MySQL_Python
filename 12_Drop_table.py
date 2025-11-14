""" Drop Tables -> The DROP TABLE statement is used to drop an existing table in a database. 
 It removes the table definition and all associated data, indexes, triggers, constraints, and permission specifications for that table."""
 
# Example 1: Drop Table in MySQL using Python

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
 
sql_query ="DROP TABLE students"

cursorObject.execute(sql_query)
dataBase.commit()

print("✅ Table 'students' dropped successfully from 'studentdb' database.")

# disconnecting from server
dataBase.close()