import mysql.connector
import matplotlib.pyplot as plt


mydb = mysql.connector.connect(host="localhost",
							user="root",
							password="",
							database="student_info")
mycursor = mydb.cursor()

mycursor.execute("select date , data from student_data")
result = mycursor.fetchall

date = []
data = []

for i in mycursor:
	date.append(i[0])
	data.append(i[1])
	


plt.bar(date, data , color="red")
# plt.ylim(0,2)
plt.xlabel("date of Students")
plt.ylabel("data of Students")
plt.title("Student's Information")
plt.show()
