age = "\nInput 'quit' when you are done."
age += "\nWhat is your age? "
message = " "
while True:
    message = input(age)
    if message == 'quit':
      break
    if int(message) < 3:
        print("Your ticket is free")
    elif int(message) <= 12:
        print("Your ticket costs 10$")
    elif int(message) > 12:
        print("Your ticket costs 15$")



