#Snow Poem Algorithm - www.101computing.net/snow-poem-algorithm
#A Python algorithm inspired by a poem by Brian Bilston: Needles"

import random

poem = "I/wrote/a poem/in the shape/of a Christmas/tree but then forgot/to water it and only a few/days/later/there/were/words/all/over/the/carpet"
author = "Brian Bilston"

#Generating a list of all the lines used in this poem
lines = poem.split("/")

print("- - - - - - Needles - - - - - - -")
print("")

#Accessing each line from the list, one at time
for i in range(0,7):
  indentation = " " * (15-len(lines[i])//2)
  print(indentation + lines[i])

#Tree Trunk
for i in range(7,9):
  indentation = " " * (15-len(lines[i])//2)
  print(indentation + lines[i])
print("")

#The last section of this poem represents the needles covering the floor
for i in range(9,len(lines)):
  indentation = random.randint(1,30) * " "
  print(indentation + lines[i])

#And the author...
print("")
print("_" * len(author))
print(author)