import re 
line ="From stephen.marquaz@uct.ac.za sat jan 509:14:16 2008"
y =re.findall("@([^ ]*)",line)
print(y)