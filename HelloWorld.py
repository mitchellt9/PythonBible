__author__ = 'Mitchell'

# #Get user inputs for name, age, place and output them
#
# a="1"
# b="Question"
# print("{} - {}".format(b,a))
#
# username=raw_input("What is your name? : ")
#
# age=raw_input("What is your age?: ")
#
# string=("The name is {} and age is {}")
# output=string.format(username,age)
# print("*"*20)
# print(output)

# Create a variable called name and set it equal to your name
name="Mitchell"

# Create a variable called age and set it to your age in years
# Note: This must be an int, not a string!
age=23

# Create a variable called place and set it equal to where you live
place="Cali"

# Create a variable called output, and use string formatting to
# make it like the example text in the description
string='"Hello my name is {} and I am {} years old. I live in {} and I love Python!'
output=string.format(name,age,place)

# Finally, use the print() function to print the output.
print(output)