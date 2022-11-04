marks = int(input("Input your marks: "))
if (marks >= 80 and marks < 90):
  print("A+")
elif marks >= 70 and marks < 80:
  print("A")
elif marks >= 60 and marks < 70:
  print("B")
elif marks >= 50 and marks < 60:
  print("C")
elif marks >= 40 and marks < 50:
  print("D")
elif (marks < 40):
 print("Failed")