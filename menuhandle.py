#!/usr/bin/python3

#this file will list the installed scripts and dynamically build a menu which
#all the .py file can be seen and chosen from

import os
from subprocess import call

Script_dir = "/home/pi/python_scripts" #we wanna list all the .py file under this directory
Script_name = os.path.basename(__file__) 

print ("Start Menu:")

scripts = []
item_number = 1 

for files in os.listdir(Script_dir): #read a list containing the names of the entries in the directory given by path
    if files.endswith(".py"):
        if files != Script_name: #exclude the menuhandle.py file from the menu
            scripts.append(files) 
            print ("%s.%s" %(item_number,files))
#            scripts.append(files)
            item_number += 1
running = True
while (running):
    print ("Please enter the script number to run: 1-%d(x to exit)" % (item_number-1))
    run_item = input()
  #  try:
    if run_item == 'x':
        running = False
        print("Exit")
    else:
        try:
           run_number = int(run_item)
           if  len(scripts) >= run_number > 0:
               commands = ["python3",scripts[run_number-1]]
#               print(commands)
               call(commands)
               running = False
           else:
               print ("the value is out of range")
        except ValueError: #just ignore the invalid input
           print("Invalid")
#end

