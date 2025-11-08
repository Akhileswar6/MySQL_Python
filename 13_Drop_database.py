"""Drop Database -> The DROP DATABASE statement is used to drop an existing entire database."""

# Example : Drop existing database in MYSQL using Python

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

sql_query = "DROP DATABASE studentdb"

cursorObject.execute(sql_query)
dataBase.commit()

print(f"💥 Database 'StudentDB' deleted successfully!")

# Close the connection
dataBase.close()

