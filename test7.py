class Point:
    def move():
        print("saai")
        
    def stop():
        print("ddddd")
        

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
point1 =Point
point1.move()
point1.stop()

print("****************")

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print("****************")

import matplotlib.pyplot as plt

# create a simple line graph
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y)

# extract the x and y limits of the graph
x_limits = plt.xlim()
y_limits = plt.ylim()
print("x limits:", x_limits)
print("y limits:", y_limits)

# extract the positions of the tick marks on the x and y axes
x_ticks = plt.xticks()
y_ticks = plt.yticks()
print("x tick positions:", x_ticks)
print("y tick positions:", y_ticks)

# extract the legend of the graph
legend = plt.legend()
print("legend:", legend)

# display the graph
plt.show()


