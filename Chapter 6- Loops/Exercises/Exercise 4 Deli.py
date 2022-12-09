sandwich_orders = ["chicken sandwich", "egg sandwich", "seafood sandwich", "nutella sandwich"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()

    print("I made your " + current_sandwiches.title() + ".")
    finished_sandwiches.append(current_sandwiches)

print("\nThe following sandwiches that were made are: ")
for made_sandwich in finished_sandwiches:
    print(made_sandwich.title())