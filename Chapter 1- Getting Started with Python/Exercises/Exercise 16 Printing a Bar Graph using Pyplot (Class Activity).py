import matplotlib.pyplot as plt

y_axis = ["Blue", "Orange", "Green", "Red"]
x_axis = [10, 20, 15, 5]

plt.bar(y_axis, x_axis, color=["blue", "orange", "green", "red"])
plt.title("The Favorite Color of Bathspa Students")
plt.ylabel("Number of Students")
plt.xlabel("Colors")
plt.show()