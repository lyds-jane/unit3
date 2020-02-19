This code is for the homework assigned on 18/02/2020.

The problem was related to graphing with python and the PyPlot module.

Here is the code:
```.py
import matplotlib.pyplot as pyplot
import random
from math import sin

# define range of x
x = [a for a in range(0, 100)]


def one():
    # question one, graphing random numbers
    y = [random.randrange(1, 100) for i in x]
    # Find average
    total = 0
    for a in y:
        total += a
    print("The average is ", total/100)
    pyplot.plot(x,y)
    pyplot.xlabel(x)
    pyplot.ylabel(y)
    pyplot.show()


def two():
    # question two, graphing this specific formula
    y = [14*sin(0.5*t) for t in x]
    pyplot.plot(x,y)
pyplot.show()


def three():
    # question three, graphing any formula
    y = [5*f + 4 for f in x]
    pyplot.plot(x, y)
pyplot.show()

one()
two()
three()
```
