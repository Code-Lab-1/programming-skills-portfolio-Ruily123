num = input("Input number: ")
factorial = 1
if int(num) < 0:
    print("Negative numbers don't have factorials.")
elif int(num) == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, int(num) + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)