number = int(input("Input a number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("This number is not a prime number.")
            break
    else:
        print("This number is a prime number.")
elif number == 0 or 1:
    print("0 and 1 is neither a prime or composite number.")
