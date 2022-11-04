usernames = ["Railey", "Dyan", "Terry", "Ice", "Admin"]
for username in usernames:
    if username == "Admin":
        print("Hello", username + ", would you like to see a status report?")
    else:
        print("Hello", username + ", thank you for logging in again.")