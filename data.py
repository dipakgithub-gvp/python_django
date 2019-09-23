import mysql.connector

mydata=mysql.connector.connect(host="localhost",user="root",password="root",database="company")

mycursor=mydata.cursor()

sql="INSERT INTO manav(id,name)values(%s,%s)"
val=(8,"bca")
mycursor.execute(sql,val)
mydata.commit()


