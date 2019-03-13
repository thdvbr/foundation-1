#!/usr/local/bin/python3 

import cgi

#get the output of the form
form = cgi.FieldStorage()

#get an input filed from the form called 'favcolor'
#and assign its value to a local variable called v_favcolor
v_favcolor = form.getvalue('favcolor')

#send an html response

print("""
<html>
<body>
<p> 
nICE, I like {} too.
</p>
</body>
</html>
""".format(v_favcolor))
