""" Order By Clause -> OrderBy is used to arrange the result set in either ascending or descending order. 
By default, it is always in ascending order unless “DESC” is mentioned, which arranges it in descending order.
“ASC” can also be used to explicitly arrange it in ascending order. But, it is generally not done this way since default already does that."""

# Example: Order By clause in MySQL using Python

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
 
sql_query = "SELECT * FROM students ORDER BY marks DESC"
cursorObject.execute(sql_query)
  
myresult = cursorObject.fetchall()
  
print("🎓 Student Records:")  
for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()
