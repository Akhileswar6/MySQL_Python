# Limit Clause -> The Limit clause is used in SQL to control or limit the number of records in the result set returned from the query generated. By default, SQL gives out the required number of records starting from the top but it allows the use of OFFSET keyword. OFFSET allows you to start from a custom row and get the required number of result rows.
# Example: Limit clause in MySQL using Python

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
 
query = "SELECT * FROM STUDENT LIMIT 2 OFFSET 1"
cursorObject.execute(query)
  
myresult = cursorObject.fetchall()
  
for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()