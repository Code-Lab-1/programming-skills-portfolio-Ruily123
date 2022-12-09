def add() :
  x = int(input("First mark: "))
  y = int(input("Second mark: "))
  r = int(input("Third mark: "))
  d = int(input("Fourth mark: "))
  average = x + y + r + d / 4
  percentage = x + y + r + d / 100 * 100
  print("The average of your marks is", average)
  print("The percentage of your marks is " + str(percentage) + "%" )

add()