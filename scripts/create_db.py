import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-prj", "--prj", type=str, required='True', 
					help="Define the name of the project")
    ap.add_argument("-db", "--db", type=str, required='True', 
					help="Define the type of database")
    args = vars(ap.parse_args())
    prj = args.get("prj")
    db = args.get("db")
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during ARGUMENT PASSING:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()

if db == 'mysql':
	with open('mydb.py', 'w+') as f:
		mystr = "import mysql.connector\n\n"
		mystr += "dataBase = mysql.connector.connect(\n"
		mystr += "	host = 'localhost',\n"
		mystr += "	user = 'root',\n"
		# PASSWORD CAN BE CHANGED FROM MAKEFILE IN THE FUTURE
		mystr += "	passwd = 'password123'\n"
		mystr += ")\n\n"
		mystr += "# Prepare cursor Object\n"
		mystr += "cursorObject = dataBase.cursor()\n\n"
		mystr += "cursorObject.execute('CREATE DATABASE "+str(prj)+"_db')\n\n"
		mystr += "print('[\033Database created successfully!')\n\033[0m"
		f.write(mystr)
elif db == 'sqlite3':
	raise Exception('\033[93m\nNeed to prepare DB sqlite3\033[0m\n')
else:
	raise Exception('\033[93m\nSelect a proper db between:\n\t-mysql\n\t-sqlite3\n\033[0m')
