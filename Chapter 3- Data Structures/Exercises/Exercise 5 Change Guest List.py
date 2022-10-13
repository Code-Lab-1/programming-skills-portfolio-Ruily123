Guests = ["Dyan","Nami", "Rami"]
message = ("Hello " + Guests[0] + ", you are invited to the dinner.")
message2 = ("Hello " + Guests[1] + ", you are invited to the dinner.")
message3 = ("Hello " + Guests[2] + ", you are invited to the dinner.")

print(message)
print(message2)
print(message3)

print("\nSadly, " + Guests[2] + " can't come to the dinner.")
del Guests[2]
Guests.insert(2, "Railey")

message = ("\nHello " + Guests[0] + ", you are invited to the dinner.")
message2 = ("Hello " + Guests[1] + ", you are invited to the dinner.")
message3 = ("Hello " + Guests[2] + ", you are invited to the dinner.")

print(message)
print(message2)
print(message3)