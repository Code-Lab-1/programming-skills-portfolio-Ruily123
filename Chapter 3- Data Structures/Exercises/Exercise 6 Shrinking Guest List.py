Guests = ["Nami","Dyan","Rami",]
message = ("Hello " + Guests[0] + ", you are invited to the dinner.")
message2 = ("Hello " + Guests[1] + ", you are invited to the dinner.")
message3 = ("Hello " + Guests[2] + ", you are invited to the dinner.")

print(message)
print(message2)
print(message3)

print("\nSadly, " + Guests[2] + " can't come to the dinner.")
del Guests[2]
Guests.insert(2, "Terry")

message = ("\nHello " + Guests[0] + ", you are invited to the dinner.")
message2 = ("Hello " + Guests[1] + ", you are invited to the dinner.")
message3 = ("Hello " + Guests[2] + ", you are invited to the dinner.")

print(message)
print(message2)
print(message3)

print("\nThe new dinner table won't arrive in time for the dinner, so I can only invite two people.")
removed_guest = Guests.pop(0)

print("\nI'm sorry " + removed_guest + ", you are no longer invited to the dinner.")
removed_guest2 = Guests.pop(1)

print("I'm sorry " + removed_guest2 + ", you are no longer invited to the dinner.")
print("\nHello " + Guests[0] + ", you are still invited to the dinner.")
del Guests[0]
print(Guests)