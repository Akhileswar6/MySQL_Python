""" To install the Python-mysql-connector module,
one must have Python and PIP, preinstalled on their system.
If Python and pip are already installed type the below command in the terminal."""

# cmd -> pip install mysql-connector-python
# cmd -> pip show mysql-connector-python


"""Connecting to MySQL Server"""


import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",                # Localhost for local connection
  user ="root",
  passwd ="Akhil@0109"
)

 
if dataBase.is_connected():
    db_Info = dataBase.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    print("Connection established successfully \n")
 
# Disconnecting from the server
dataBase.close()
