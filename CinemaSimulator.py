__author__ = 'Mitchell'

films={
    "Finding Nemo":{"age":3,"seats":10},
    "Death Race":{"age":21,"seats":20},
    "Finding Neverland":{"age":13,"seats":10}
}

while True:
    choice=raw_input("Which movie do you want to watch Today? ").title()

    if choice in films: #Check if the user input is in the films dictionary
        attendee_age=int(raw_input("What is your age? ")) #raw input always sends the input as String, so cast it
        if attendee_age >= films[choice]["age"]:

            ticket_count=int(raw_input("How many tickets do you want? "))
            if ticket_count>films[choice]["seats"]:
                print("We have no tickets left!")
            else:
                films[choice]["seats"]=films[choice]["seats"]-ticket_count
                print("ENJOY THE SHOW")
        else:
            print("You are underage")
    else:
        print("The film is not being aired here!")
