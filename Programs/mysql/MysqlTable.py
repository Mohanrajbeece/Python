import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "$Monirm7$",db="TEST")  
  
#creating the cursor object  
cur = myconn.cursor()  
"""key="INSERT INTO customers(name,address) VALUES(%s, %s)"
value=[("moni","chennai"),("pooja","vellore"),("nisha","ve")]""" 
try:  
    #Creating a table with name Employee having four columns i.e., name, id, salary, and department id  
    #dbs = cur.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")
    #dbs = cur.execute("SHOW TABLES")
    #dbs= cur.execute("DESC customers")
    dbs = cur.execute("SELECT * FROM customers WHERE address ='vellore'")
    myconn.commit() 
except:  
    print("Error") 
for i in cur:
    print(i)
myconn.close()  
