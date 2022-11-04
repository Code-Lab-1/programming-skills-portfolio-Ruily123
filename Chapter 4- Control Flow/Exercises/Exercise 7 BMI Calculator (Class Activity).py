weight = int(input("Weight in kg: "))
height = int(input("Height in cm: "))

formula = weight / height**2 * 10000

if formula <= 18.5:
    print("Underweight")
elif (formula >= 18.5 and formula < 25):
    print("Normal")
elif (formula >= 25 and formula < 30):
    print("Overweight")
elif (formula > 30):
    print("Obese")