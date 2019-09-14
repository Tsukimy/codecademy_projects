"""
The program is analogue of game 'Rock, Paper, Scissors', where computer randomly chooses the subject and the user tries to guess it.
The program compares results and determines the winner.
After - informs.
"""

from random import randint
from time import sleep

options = ["R", "P", "S"]
l = "You lost!"
w = "You won!"

def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "Computer selected: %s" % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
    print w
  elif user_choice_index == 1 and computer_choice_index == 0:
    print w
  elif user_choice_index == 2 and computer_choice_index == 1:
    print w
  elif user_choice_index > 2:
    print "Invalid meaning!"
    return
  else:
    print l
    
def play_RPS():
  print "Rock, Paper, Scissors."
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
  sleep(1)
  user_choice = user_choice.upper()
  # computer_choice = options[randint(0,2)]
  computer_choice = options[randint(0, len(options)-1)]
  decide_winner(user_choice, computer_choice)

  
play_RPS()