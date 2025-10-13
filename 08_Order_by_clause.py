# Order By Clause -> OrderBy is used to arrange the result set in either ascending or descending order. By default, it is always in ascending order unless “DESC” is mentioned, which arranges it in descending order. “ASC” can also be used to explicitly arrange it in ascending order. But, it is generally not done this way since default already does that.
# Example: Order By clause in MySQL using Python

# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Akhil@0109",
  database = "gfg"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
 
query = "SELECT * FROM STUDENT ORDER BY NAME DESC"
cursorObject.execute(query)
  
myresult = cursorObject.fetchall()
  
for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()
