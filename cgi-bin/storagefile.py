#!/usr/bin/python3
import cgi, cgitb 
import time
import random

def get_temp(data):
	return float(data[0:5])

print("Content-type: text/html\r\n\r\n") 
print("<html><head><style>")
print("td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}")
print("</style></head>")
print("<body>")
form = cgi.FieldStorage() 
number_input = form.getvalue('number_message')

# Form for input
print("<form method = 'post' ")
print("<p>Input Number: <input type='text' name='number_message'/></p>") 
print("<input type='submit' value='Enter' />") 
print("</form>")

# Check number is not alphabet
try:
	float(number_input)
	f = open('data.txt','a+')
	f.write(str(number_input))  # Add number
	f.write("    "+ time.ctime())  # Add time
	#f.write("<br>")
	f.write("\n")
	f.close()
except:	
	print("<h1>"+"Please enter only number!"+"</h1><br>")  # Show when enter alphabet

# Read file to web page
readed = open('data.txt','r')
role=[]#list of templature
date=[]#list of date
temp = []
for i in readed:
	temp.append(i)
temp.sort(key=get_temp,reverse=True)

for i in temp:
    role.append(float(i[0:5]))
    date.append(i[5:-5])


print("In File:")
print("<table>")
print("<tr>")
print("<th>Date</th>")
print("<th>Templature(C)</th>")
print("</tr>")
print("<tr>"+"<td>>"+str(random.randrange(0,10))+"</t1d>" + "<td>"+str(random.randrange(0,10))+"</td>"+"</tr>")  # test random

for i in range(len(role)):
	print("<tr>")
	print("<td>>"+date[i]+"</t1d>")
	print("<td>"+str(role[i])+"</td>")
	print("</tr>")


print("</table>")
print("</body></html>") 

readed.close()


