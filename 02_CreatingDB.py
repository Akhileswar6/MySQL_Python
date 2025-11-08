""" Creating Database -> After connecting to the MySQL server let's see how to create a MySQL database using Python.
For this, we will first create a cursor() object and will then pass the SQL command as a string to the execute() method. """

# Creating MySQL database with Python

import mysql.connector
 
# Connect to MySQL Server
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109"
)

# Create a cursor object to execute SQL queries
cursorObject = dataBase.cursor()

# Create a new database
cursorObject.execute("CREATE DATABASE StudentDB")

print("✅ Database 'StudentDB' created successfully!")

dataBase.close()


