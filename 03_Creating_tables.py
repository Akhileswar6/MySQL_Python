""" Creating Tables -> Creating MySQL table using Python """

import mysql.connector
 
# Connect to the database you created
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109",
  database = "studentdb"
)

# Create a cursor object
cursorObject = dataBase.cursor()
 
# creating table 
studenttable = """CREATE TABLE students (
                   student_id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(100),
                   branch VARCHAR(50),
                   roll_no INT,
                   marks INT
                   )"""
 
# table created
cursorObject.execute(studenttable)

print("✅ Table 'students' created successfully in 'studentdb' database.")
 
# disconnecting from server
dataBase.close()