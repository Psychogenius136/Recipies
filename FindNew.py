import sqlite3
from sqlite3 import Error


def create_connection(path):

    connection = None

    try:

        connection = sqlite3.connect(path)

        print("Connection to SQLite DB successful")

    except Error as e:

        print(f"The error '{e}' occurred")


    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.executescript(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")



def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")






create_users_table = """
CREATE TABLE IF NOT EXISTS inventory (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Name TEXT,
  NiceName TEXT,
  Reward TEXT,
  Level INTEGER,
  Img_Location TEXT,
  Inventory_Slot  INTEGER,
  Bonus TEXT
);
"""
insert = """
select * from Stash where Name="None";          
"""

#insert = "select Cordx,Cordy from Empowering_Minions ; "

drd="""
CREATE TABLE IF NOT EXISTS Toxic (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
"""

connection = create_connection("inventory.sqlite")
#execute_query(connection, create_users_table) 
#execute_query(connection, drd)  
ddd =execute_read_query(connection, insert)  
print (ddd)