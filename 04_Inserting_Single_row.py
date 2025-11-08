""" Insert Data into Tables """
# Example 1: Inserting Single Row

# Connect to StudentDB database
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109",
  database = "studentdb"
)

# Create a cursor object
cursorObject = dataBase.cursor()
 
insert_query = """
INSERT INTO students (name, branch, roll_no, marks) 
VALUES ('Akhileswar', 'CSE', 101, 95)"""
  
cursorObject.execute(insert_query)

# Commit the changes to make sure data is saved
dataBase.commit()

print("✅ Record inserted successfully into 'students' table!")

# Close the connection
dataBase.close()


