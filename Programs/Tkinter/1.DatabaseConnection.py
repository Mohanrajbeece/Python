"""import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "$Monirm7$")  
  
#printing the connection object   
print(myconn) """

import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "$Monirm7$")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    dbs = cur.execute("show databases")  
except:  
    myconn.rollback()  
for x in cur:  
    print(x)  
myconn.close()  
