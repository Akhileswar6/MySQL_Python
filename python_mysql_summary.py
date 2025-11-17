# ---------------------------------------------------------
#  MySQL + Python Full Tutorial
#  Author: Akhileswar Kamale
#  Description: Connect, Create DB, Tables, Insert, Fetch,
#               Update, Delete, Drop using mysql-connector
# ---------------------------------------------------------

import mysql.connector

# ---------------------------------------------------------
# 1️⃣ Connect to MySQL Server
# ---------------------------------------------------------
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Akhil@0109"
)

print("✅ Connected to MySQL Server successfully!")

# ---------------------------------------------------------
# 2️⃣ Create a Database
# ---------------------------------------------------------
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE StudentDB")
print("✅ Database 'StudentDB' created successfully!\n")

# ---------------------------------------------------------
# 3️⃣ Connect to the New Database
# ---------------------------------------------------------
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Akhil@0109",
    database="StudentDB"
)
cursorObject = dataBase.cursor()
print("✅ Connected to 'StudentDB' database.\n")

# ---------------------------------------------------------
# 4️⃣ Create a Table
# ---------------------------------------------------------
cursorObject.execute("""
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    branch VARCHAR(50),
    roll_no INT,
    marks INT
)
""")
print("✅ Table 'students' created successfully!\n")

# ---------------------------------------------------------
# 5️⃣ Insert a Single Record
# ---------------------------------------------------------
cursorObject.execute("""
INSERT INTO students (name, branch, roll_no, marks)
VALUES ('Akhileswar', 'CSE', 101, 95)
""")
dataBase.commit()
print("✅ Single record inserted successfully!\n")

# ---------------------------------------------------------
# 6️⃣ Insert Multiple Records
# ---------------------------------------------------------
insert_query = """
INSERT INTO students (name, branch, roll_no, marks)
VALUES (%s, %s, %s, %s)
"""
student_data = [
    ("Rohit", "ECE", 102, 88),
    ("Sneha", "MECH", 103, 91),
    ("Kiran", "CSE", 104, 85),
    ("Divya", "IT", 105, 90)
]
cursorObject.executemany(insert_query, student_data)
dataBase.commit()
print(f"✅ {cursorObject.rowcount} records inserted successfully!\n")

# ---------------------------------------------------------
# 7️⃣ Fetch All Records
# ---------------------------------------------------------
cursorObject.execute("SELECT * FROM students")
result = cursorObject.fetchall()
print("🎓 All Student Records:")
for row in result:
    print(row)
print()

# ---------------------------------------------------------
# 8️⃣ Update a Record
# ---------------------------------------------------------
cursorObject.execute("""
UPDATE students
SET marks = 92
WHERE name = 'Kiran'
""")
dataBase.commit()
print(f"✅ Record updated successfully! Rows affected: {cursorObject.rowcount}\n")

# ---------------------------------------------------------
# 9️⃣ Delete a Record
# ---------------------------------------------------------
cursorObject.execute("DELETE FROM students WHERE name = 'Rohit'")
dataBase.commit()
print(f"🗑️ Record deleted successfully! Rows affected: {cursorObject.rowcount}\n")

# ---------------------------------------------------------
# 🔟 Drop Table
# ---------------------------------------------------------
cursorObject.execute("DROP TABLE students")
print("🧨 Table 'students' deleted successfully!\n")

# ---------------------------------------------------------
# 1️⃣1️⃣ Drop Database
# ---------------------------------------------------------
cursorObject.close()
dataBase.close()

# Reconnect to MySQL Server (not StudentDB)
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Akhil@0109"
)
cursorObject = dataBase.cursor()
cursorObject.execute("DROP DATABASE StudentDB")
print("💥 Database 'StudentDB' deleted successfully!\n")

# ---------------------------------------------------------
# ✅ Close Connection
# ---------------------------------------------------------
dataBase.close()
print("🔒 MySQL connection closed successfully.")
