__author__ = 'Mitchell'

known_users=["mitchell","keshav","ankit"]

while True:
    user_input=raw_input("Enter your name: ").strip().lower()

#Gatekeeping
    if user_input in known_users:
        string_accept="Hello {}, good to have you onboard!"
        print(string_accept.format(user_input))

    #Checking if user wants to be in the System
        system_accept=raw_input("Do you want to be in the System? (y/n): ").lower()
        if system_accept=="y":
            print("Keeping you in the System")
        else:
            known_users.remove(user_input)
            print("Sorry to see you go!")

    else:
        string_reject="Hey {}. You do not have the permission to enter."
        print(string_reject.format(user_input))

        system_add=raw_input("Do you want to be a part of the system? y/n: ")
        if system_add=="y":
            known_users.append(user_input)
            print("You have been added successfully into the System, {}").format(user_input)
        else:
            print("Too bad! Bye")

