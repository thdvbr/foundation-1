#!/usr/bin/env python3
import cgi
import csv 

#get the output of the form
form = cgi.FieldStorage()

#get an input filed from the form called 'color'
#assign its value to a local var called v_color
v_color = form.getvalue('color').lower()

if ' ' in v_color:
    v_color = v_color.replace(' ','_')

#read csv file 
#check if v_color matches each color name in csv file
#if not continue the loop, if found return True 


with open('scripts/colors.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        if v_color in line:
            found = True
            break
        else: 
            found = False
            
            
    
#send an html response
 
if found:
        print("""
            <html>
            <body>
            <p>{} is a color
            </p>
            </body>
            </html>""".format(v_color))
else:
        print("""
            <html>
            <body>
            <p>{} is not a color
            </p>
            </body>
            </html>""".format(v_color))
            