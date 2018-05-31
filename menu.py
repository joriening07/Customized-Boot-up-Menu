#!/usr/bin/python3

from subprocess import call

filename='menu.ini'

DESC=0
KEY=1
CMD=2

print("Start Menu:")
#Show all the check option in the file
try:
    with open(filename) as f:
        menufile = f.readlines()
except IOError:
    print ("Unable to open %s" %(filename))
for item in menufile:
    line = item.split(',')
    print ("(%s):%s" % (line[KEY],line[DESC]))

#get user input, check it and run the according command.
running = True
while(running):
    user_input = input()
    for item in menufile:
        line = item.split(',')
        if (user_input.lower() == line[KEY]):
            print ("Command:" + line[CMD])
            #call the script
            commands = line[CMD].rstrip().split()
            print(commands)
          #  call(commands)
            if len(commands):     #if command is none(in menu.ini), meaning we choose to exit.
                call(commands)    #only rn command when one exits
            elif (user_input.lower() == 'e'):
                running = False
            else:
                print ("Key is not in menu.")
                running = False
print("Finished")
#end

