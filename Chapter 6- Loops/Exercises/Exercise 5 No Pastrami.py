sandwich_orders = ["pastrami sandwich", "chicken sandwich", "egg sandwich", "pastrami sandwich", "seafood sandwich",
                   "nutella sandwich", "pastrami sandwich"]
print(sandwich_orders)
print("\nThe deli has run out of pastrami sandwiches.")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
print(sandwich_orders)
