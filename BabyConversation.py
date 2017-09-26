__author__ = 'Mitchell'
import random

questions=["What is your name? ","Favorite Color? ", "What is your Hobby? "]

#For Random set of questions
# questions=random.choice(questions)
# answer=raw_input(questions)

for i in range(len(questions)):
    answer=raw_input(questions[i]).strip().lower()
    i=i+1
    while answer != "just because":
        answer=raw_input("Why?")
    print("Hope that sorted you out!")
