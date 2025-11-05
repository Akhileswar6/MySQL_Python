""" Insert Data into Tables """
# Example 1: Inserting Single Row

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
 
sql = "INSERT INTO student1 (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = ("Akhileswar", "CSC", "07", "B", "19")
  
cursorObject.execute(sql, val)
dataBase.commit()
  
# disconnecting from server
dataBase.close()



