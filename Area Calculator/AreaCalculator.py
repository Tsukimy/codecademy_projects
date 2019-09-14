print "The program allows you to choose the form and calculate its area"

from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()

print "The calculation is starting!"
print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."
option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == "C":
    radius = float(raw_input("Enter the radius:"))
    area = pi * radius**2
    print "The pie is baking..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
elif option == "T":
    base = float(raw_input("Enter the base: "))
    height = float(raw_input("Enter the height: "))
    area = base*height*(0.5)
    print "Uni Bi Tri..."
    print ("Area: %.2f. \n%s" % (area, hint))
else:
    print "The garbage is entered. Exiting."