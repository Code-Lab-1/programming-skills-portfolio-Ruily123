toppings = "\nInput 'quit' when you are satisfied with the amount of toppings."
toppings += "\nWhat pizza toppings would you like on your pizza? "
message = " "
while message != "quit":
    message = input(toppings)
    print(message.title(), "will be added to your pizza. ('quit' will not be added to your pizza)\n")