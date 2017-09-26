__author__ = 'Mitchell'

# word="MarcusRashford"
# print(word[2])
#print(word[6:10:1]) #Code to slice the word Rash
#print(word[:word.index("R")])

#Get the username as console input
username=raw_input("Enter your email id: ")
# username="mitchell.thomas@webyog.com"
# var=username[0:1:1]
# print(var)

# #Save the name and domain as independent variables using slices
name=username[0:username.index("@")]
name=name[0:name.index(".")] #This logic will fail for non period containing email ids
name=name.title()


domain=username[username.index("@")+1:username.index(".com")]

#OR use the strip function to remove the @ symbol
# domain=domain.strip("@")
domain=domain.title()

#Use string format method to format the output
string="The username is {} and domain he belongs to is {}"
print(string.format(name,domain))


