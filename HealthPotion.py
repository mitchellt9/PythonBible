__author__ = 'Mitchell'

import random

health=50
difficulty=random.randint(1,3)
print("The difficulty level is:"+str(difficulty))

potion= random.randint(25,50)/difficulty
health=health+potion
print('Current health is: '+str(health))

