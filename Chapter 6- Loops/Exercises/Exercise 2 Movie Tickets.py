age = "\nInput 'quit' when you are done."
age += "\nWhat is your age? "
message = " "
while message !="quit":
    message = input(age)
    if int(message) < 3:
     print("Your ticket is free")
    elif int(message) <= 12:
     print("Your ticket costs 10$")
    elif int(message) > 12:
     print("Your ticket costs 15$")


