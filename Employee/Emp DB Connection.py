import mysql.connector

mydb = mysql.connector.connect(host="Sush Database",user="root",password="sush123")

mycursor = mydb.cursor()

#mycursor.execute("EmployeeDB")
mycursor.execute("Select * from EmployeeDB.employee")

for i in mycursor:
    print(i)