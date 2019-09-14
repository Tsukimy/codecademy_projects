"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "The story is starting right now!"

name = raw_input("What is your name? ")
adj1 = raw_input("Type three different adjectives separately, first is: ")
adj2 = raw_input("Time for second one: ")
adj3 = raw_input("And the third: ")
verb = raw_input("Let us type a verb: ")
noun1 = raw_input("A noun: ")
noun2 = raw_input("And one more noun: ")
animal = raw_input("Well, time to continue Type an animal: ")
food = raw_input("...a kind of food..: ")
fruit = raw_input("...a fruit..: ")
superhero = raw_input("...your favourite superhero: ")
country = raw_input("..any country..: ")
dessert = raw_input("...sweet dessert..: ")
year = raw_input("..and a year..: ")

print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)