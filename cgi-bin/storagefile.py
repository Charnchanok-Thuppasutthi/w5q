#!/usr/bin/python3
import cgi, cgitb 
import time
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
print("</form>  ")

# Check number is not alphabet
try:
	int(number_input)
	isNumber = True
	str(number_input)
except:
	isNumber = False
	
# Add text in file
if (isNumber == True):	
		# Write if number is not alphabet
		f = open('data.txt', 'a+')
		f.write(number_input)  # Add number
		f.write("  "+ time.ctime())  # Add time
		f.write("<br>")
		f.write("\n")
		f.close()
elif (number_input != None):
	print("<h1>"+"Please enter only number!"+"</h1><br>")  # Show when enter alphabet

# Read file to web page
readed = open('data.txt', 'r')
temp=[]#list of templature
date=[]#list of date
for i in readed:
    temp.append(i[0:3])
    date.append(i[3:-5])

print("In File:")
print("<table>")
print("<tr>")
print("<th>Templature(C)</th>")
print("<th>Date</th>")
print("</tr>")

for i in range(len(temp)):
	print("<tr>")
	print("<td>"+temp[i]+"</td>")
	print("<td>>"+date[i]+"</t1d>")
	print("</tr>")


print("</table>")
print("</body></html>") 

readed.close()


