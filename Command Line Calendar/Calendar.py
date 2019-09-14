"""
This program representates itself like a calendar.
It allows to view it, add, update and delete events.
"""
from time import sleep, strftime
name = "tsukimy"

calendar = {}
def welcome():
  print "Welcome, " + name + "!"
  print "The calendar is opening..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print "Now is: " + strftime("%H:%M:%S")
  sleep(1)
  print "What would you like ti do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Type A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "The calendar is empty"
      else:
        print calendar
    elif user_choice == 'U':
      date = raw_input("What date? ")
      update = raw_input("Enter update: ")
      calendar[date] = update
      print "Update has been successful!"
      print calendar
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:])<int(strftime("%Y"))):
        print "Invalid date entered"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.uppercase()
        if try_again == 'Y':
          continue
        #elif try_again == 'N':
         #exit
        else:
          start = False
      else:
        calendar[date] = event
        print "The event was successfully added"
        print calendar
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print "The calendar is empty"
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "The event has successfully deleted"
            print calendar
          else:
            print "Invalid event"
    elif user_choice == 'X':
      update = start
    else:
      print "Invalid command"
      exit
      
start_calendar()
