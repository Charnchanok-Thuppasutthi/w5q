#!/usr/bin/python3
import cgi, cgitb 
print("Content-type: text/html\r\n\r\n") 
print("<html><body>")

form = cgi.FieldStorage() 
number = form.getvalue('input')



print("<form method = 'post' ")
print("<p>Input: <input type='text' name='input' /></p>") 
print("<input type='submit' value='Submit' />") 
print("</form>  ")

f = open('data.txt', 'a+')
f.write(number)
f.write("<br>")
f.close()

r = open('data.txt', 'r')
s = r.read()
print("In File:")
print("<h1>"+s+"</h1><br>")
r.close()

print("</body></html>") 

