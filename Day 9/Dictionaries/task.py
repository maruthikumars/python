programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}


print(programming_dictionary["Bug"])

programming_dictionary["loop"] = "test"
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "Test"
print(programming_dictionary)

#Loop through dictionary
for thing in programming_dictionary:
    print(thing) #just keys
    print(programming_dictionary[thing]) #value

empty_dictionary = {}

#Empty dictionary
programming_dictionary = {}
print(programming_dictionary)

