#!/usr/bin/python
 # -*- coding: UTF-8 -*-
import re
 
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
print ("你好，世界")

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("fj")

   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
print ("你好，世界")