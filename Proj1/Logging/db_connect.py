import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "logs"
)

cursor = conn.cursor()



cursor.close()
conn.close()