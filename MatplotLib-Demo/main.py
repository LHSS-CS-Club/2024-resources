# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:
import matplotlib.pyplot as plt

# we will use some functions from numpy as well:
import numpy as np

# The plot() function is used to draw points (markers) in a diagram. By default, the plot() function draws a line from point to point.
### plot a line from (1, 3) to (8, 10) ###

xRange = np.array([1, 8])
yRange = np.array([3, 10])
plt.plot(xRange, yRange)
plt.show() 


### this draws the point without connecting ###
""" 
xRange = np.array([1, 8])
yRange = np.array([3, 10])
plt.plot(xRange, yRange, 'o')
plt.show()
"""

# Use a marker, can also use X,+,s,D etc, visit documentation
"""
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
"""

# linestyle or ls, changes the style of the plotted line:
"""ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle='dotted')
plt.plot(ypoints, linestyle='dashed')
plt.show()"""

# use c parm to change the color (140 colours), can take in a hex
"""ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle='dashed', c='blue')
plt.show()"""

# you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
"""x = np.array([80, 85, 40, 97, 110, 105, 110, 115, 120, 135])
y = np.array([240, 250, 260, 270, 270, 295, 305, 315, 325, 320])

plt.plot(x, y)

plt.xlabel("Some x label")
plt.ylabel("Output")

plt.show()"""

# you can use the scatter() function to draw a scatter plot.
"""
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
"""

# you can compare 2 datasets
"""
#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)
plt.show()"""

# simple bar graph
"""
chat = np.array(["A", "B", "C", "D"])
amount = np.array([3, 8, 1, 10])

plt.bar(chat,amount)
plt.show()"""

# simple pie graph
"""
distribution = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()
"""

# pie graph with labels
"""
distribution = np.array([35, 25, 25, 15])
mylabels = ["Coca Cola", "Pepsi", "Root beer", "Sprite"]


plt.pie(y)
plt.show()
"""
