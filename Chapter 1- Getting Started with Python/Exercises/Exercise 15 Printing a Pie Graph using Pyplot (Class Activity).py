import matplotlib.pyplot as plt

y = [10, 20, 15, 5]
mylabels = ["Blue", "Orange", "Green", "Red"]

plt.pie(y, labels = mylabels, autopct='%1.1f%%')
plt.title("The Favorite Color of Bathspa Students")
plt.show()