import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password123'
)

# Prepare cursor Object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_db")

print('Database created successfully!')
