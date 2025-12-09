import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="sush123")


mycursor = mydb.cursor()

#mycursor.execute("info")
mycursor.execute("Select * from EmployeeDB.employee")

for i in mycursor:
    print(i)