""" Creating Tables -> Creating MySQL table using Python """

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
 
# creating table 
studentRecord = """CREATE TABLE STUDENT1 (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT PRIMARY KEY,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""
 
# table created
cursorObject.execute(studentRecord) 
 
# disconnecting from server
dataBase.close()