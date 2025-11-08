# Example 2: Inserting Multiple Rows

import mysql.connector
 
# Connect to the StudentDB database
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109",
  database = "studentdb"
)

# Create a cursor object
cursorObject = dataBase.cursor()
 
insert_query = """INSERT INTO students (name, branch, roll_no, marks) 
VALUES (%s, %s, %s, %s)"""

# List of tuples containing multiple student records
student_data = [
    ("Rohit", "ECE", 102, 88),
    ("Sneha", "MECH", 103, 91),
    ("Kiran", "CSE", 104, 85),
    ("Divya", "IT", 105, 90)
]

  
cursorObject.executemany(insert_query, student_data)

# Commit the changes
dataBase.commit()

print(f"✅ {cursorObject.rowcount} records inserted successfully into 'students' table!")

# Close the connection
dataBase.close()