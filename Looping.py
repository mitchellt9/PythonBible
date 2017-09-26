__author__ = 'Mitchell'

students={
    "male":["Jack","Jones","Johnny"],
    "female":["Jini","Jessi","Gani"]
}

#Loops to determine if a letter is present in the given strings in the dictionary
for a in students.keys():
    for b in students[a]:
        if "j" in b:
            print(b)
