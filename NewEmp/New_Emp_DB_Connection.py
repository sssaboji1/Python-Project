import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="sush123")


mycursor_employee = mydb.cursor()
mycursor_Department = mydb.cursor()
mycursor_Role = mydb.cursor()
mycursor_Shift = mydb.cursor()
mycursor_EmployeeShift = mydb.cursor()

#mycursor.execute("info")
mycursor_employee .execute("Select * from EmployeeDB.Employee")
for i in mycursor_employee:
    print(i)        

mycursor_Department .execute("Select * from EmployeeDB.Department")
for i in mycursor_Department:
    print(i)      

mycursor_Role .execute("Select * from EmployeeDB.Role")
for i in mycursor_Role:     
    print(i)    

mycursor_Shift .execute("Select * from EmployeeDB.Shift")
for i in mycursor_Shift:
    print(i)    

mycursor_EmployeeShift.execute("Select * from EmployeeDB.EmployeeShift")
for i in mycursor_EmployeeShift:        
    print(i)  

    
